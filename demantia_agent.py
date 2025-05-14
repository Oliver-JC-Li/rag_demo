"""
This is a script to create a multi-agents QA chatbot for demantia caregivers. Specifically, it contain a resource
agent that fetch information for a curated list of URLs, and a manual agent that extract information from demantia
manual.
"""

import streamlit as st

from langchain_community.document_loaders import WebBaseLoader, PyPDFLoader
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI, OpenAI, OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_community.callbacks.streamlit import StreamlitCallbackHandler

from langchain_core.messages import AIMessage, SystemMessage
from langgraph.graph import MessagesState, StateGraph, END, START
from langgraph.checkpoint.memory import MemorySaver

from typing import Annotated
from operator import add


openai_api_key = st.secrets["OPENAI_API_KEY"]

# Resource Agent using CSV Loader
# Index the document and store it in vector store
docs = CSVLoader("./star_c/resources.csv").load_and_split()
vector_store = FAISS.from_documents(docs, embedding=OpenAIEmbeddings())

llm = ChatOpenAI(model="gpt-4o-mini")
retriever = vector_store.as_retriever(
    search_kwargs={"k": 2}
)

system_prompt = """
    You are an assistant for question-answering tasks.
    Use the following pieces of retrieved context to answer
    the question. If you don't know the answer,  please say 
    "The study material does not contain this information"
    Only return a numbered list of URL from the retrieved context 
    to answer user's question.
    \n\n
    {context}
"""

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{input}")
])

qa_chain = create_stuff_documents_chain(llm, prompt)
url_rag_chain = create_retrieval_chain(retriever, qa_chain)


def extract_url(ans_text):
    """

    :param ans_text: A numbered list of URLs in text format
    :return: A list of URL
    """
    url_ls = []
    temp_list = ans_text.split("\n")
    for url in temp_list:
        url_ls.append(url.split(". ")[1])
    return url_ls


# WebPage RAG
def web_rag(url_list):
    # Index the document and create vector store
    web_docs = WebBaseLoader(
        web_path=(url_list),
    ).load()

    doc_chunks = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=20).split_documents(web_docs)
    web_vector_store = FAISS.from_documents(doc_chunks, embedding=OpenAIEmbeddings())

    llm = ChatOpenAI(model="gpt-4-turbo")
    web_retriever = web_vector_store.as_retriever()
    w_system_prompt = """
    You are a consultant with a master’s degree or equivalent in counseling, psychology, or social work, 
    with clinical experience working with older adults. You will be answering questions from family 
    caregivers of older adults living with Alzheimer's disease and related dementias.
    
    Please follow these response rules:
    1. If the answer can be found in the knowledge base, respond in the following format:
        Answer: [Your answer based on the knowledge]
    2. If the answer cannot be found in the knowledge base, you must reply exactly with the following format:
        Answer: "The STAR-C materials don’t have this information, I’ll also ask the STAR-C coach to check in with 
                 you to make sure your question gets answered. However, here's the possible answer to your question"
                 Then use your world knowlege to provide possible answer
    3. Write at a 6th to 8th grade reading level. Avoid medical jargon. If a medical term must be used, 
       define it simply.
    4. Use an empathetic and supportive tone. Make the caregiver feel heard, respected, and understood.
    \n\n
    {context}
    """

    w_prompt = ChatPromptTemplate.from_messages([
        ("system", w_system_prompt),
        ("human", "{input}")
    ])

    w_qa_chain = create_stuff_documents_chain(llm, w_prompt)
    w_rag_chain = create_retrieval_chain(web_retriever, w_qa_chain)

    return w_rag_chain


# AZ QA Agent
# Index document and define vector store
training_doc = PyPDFLoader("./star_c/demantia_training.pdf").load()
t_doc_chunk = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=20).split_documents(training_doc)
t_vector_store = FAISS.from_documents(t_doc_chunk, embedding=OpenAIEmbeddings())
llm = ChatOpenAI(model="gpt-4-turbo")

training_retriever = t_vector_store.as_retriever()
t_system_prompt = """
    You are an assistant for question-answering tasks. Use only the following pieces of retrieved context 
    to answer the question. If you don't know the answer, please say 
    "OOD_FLAG" Then use your world knowledge to provide possible answer.
    \n\n
    {context}
"""
t_prompt = ChatPromptTemplate.from_messages([
    ("system", t_system_prompt),
    ("human", "{input}")
])

t_qa_chain = create_stuff_documents_chain(llm, t_prompt)
t_rag_chain = create_retrieval_chain(training_retriever, t_qa_chain)


# Define Graph Logic
class State(MessagesState):
    responses: Annotated[list[dict], add]


def resource_rag(state: State):
    url_ans = url_rag_chain.invoke({"input": state['messages'][-1].content})
    retrieved = False if "http" not in url_ans['answer'] else True
    if retrieved:
        url = extract_url(url_ans['answer'])
    
        web_rag_chain = web_rag(url)
        response = web_rag_chain.invoke({"input": state['messages'][-1].content})
        resource = [doc.metadata['source'] for doc in response['context']]
        return {
            "responses":[{
                "agent": "web_resourceRAG",
                "is_from_source": True,
                "response": response['answer'],
                "resources": set(resource)
            }]
        }
    else:
        return {
            "responses":[{
                "agent": "web_resourceRAG",
                "is_from_source": False,
                "response": "The STAR-C materials don’t have this information, I’ll ask theSTAR-C coach to check in with you to make sure your question gets answered."
            }]
        }


def training_rag(state: State):
    response = t_rag_chain.invoke({"input": state['messages'][-1].content})
    if "OOD_FLAG" not in response['answer']:
        resource = [doc.metadata['source'] for doc in response['context']]
        return {
            "responses": [{
                "agent": "bookletRAG",
                "is_from_source": True,
                "response": response['answer'],
                "resources": set(resource)
            }]
        }
    else:
        return {
            "responses": [{
                "agent": "bookletRAG",
                "is_from_source": False,
                "response": response['answer'].split("OOD_FLAG")[1],
            }]
        }


def summarize(state: State):
    llm = ChatOpenAI(model="gpt-4-turbo")
    messages = []
    agent_1_r = state['responses'][-1]
    agent_2_r = state['responses'][-2]

    agent1_from_source = agent_1_r.get("is_from_source")
    agent1_response = agent_1_r.get("response", "")
    agent1_resouce = agent_1_r.get("resources", "No resources used")

    agent2_from_source = agent_2_r.get("is_from_source")
    agent2_response = agent_2_r.get("response", "")
    agent2_resource = agent_2_r.get("resources", "No resources used")

    response_prefix = False
    
    if not agent1_from_source and agent2_from_source:
        ans = f"Source: {agent2_resource}\nResponse: {agent2_response}"
        messages.append(AIMessage(content=ans))
    elif agent1_from_source and not agent2_from_source:
        ans = f"Source: {agent1_resouce}\nResponse: {agent1_response}"
        messages.append(AIMessage(content=ans))
    elif not agent1_from_source and not agent2_from_source:
        response_prefix = True
        ans1 = f"Source: {agent1_resouce}\nResponse: {agent1_response}"
        ans2 = f"Source: {agent2_resource}\nResponse: {agent2_response}"
        messages.append(AIMessage(content=ans1))
        messages.append(AIMessage(content=ans2))
    else:
        ans1 = f"Source: {agent1_resouce}\nResponse: {agent1_response}"
        ans2 = f"Source: {agent2_resource}\nResponse: {agent2_response}"
        messages.append(AIMessage(content=ans1))
        messages.append(AIMessage(content=ans2))

    system_message = ("""
    You are a helpful assistant. Use the following AI-generated responses, which include sourced information, to answer the user’s question. 
    Your goal is not to summarize what each response said, but to synthesize a clear, informative, and direct answer based on the available information. 
    Please follow the below guidelines:
    1. If multiple perspectives are provided, integrate them to form a complete response. 
    2. Write at a 6th to 8th grade reading level. Avoid medical jargon. If a medical term must be used, 
    define it simply. 
    3. Rely strictly on the provided text, without including external information.
    4. In the end, include resources used to generate the answer
    """)
    
    
    response_OOD = "The STAR-C materials don’t have this information, I’ll ask the STAR-C coach to check in with you to make sure your question gets answered. However, here's the possible answer.\n"
    prompt = [SystemMessage(content=system_message), 
              state['messages'][-1]] + messages
    response = llm.invoke(prompt)
    ans = response.content if not response_prefix else response_OOD + response.content
    return {"messages": [AIMessage(content=ans)]}


graph_builder = StateGraph(MessagesState)

graph_builder.add_node("resource_rag", resource_rag)
graph_builder.add_node("training_rag", training_rag)
graph_builder.add_node("summarize", summarize)

graph_builder.add_edge(START, "resource_rag")
graph_builder.add_edge(START, "training_rag")
graph_builder.add_edge("resource_rag", "summarize")
graph_builder.add_edge("training_rag", "summarize")
graph_builder.add_edge("summarize", END)

memory = MemorySaver()
graph = graph_builder.compile(checkpointer=memory)


# Streamlit framework
st.title("VSA with Resource and Booklet Agents to assist demantia caregivers")
config = {"configurable": {"thread_id": "abc123"},
          "callback": [StreamlitCallbackHandler(st.container())]}
# Create and store chat history and vector db in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# Display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Get user input and chatbot response
if prompt_ := st.chat_input("Please ask any question"):

    st.chat_message("user").markdown(prompt_)

    st.session_state.chat_history.append({"role": "user", "content": prompt_})

    output = graph.invoke({"messages": [{"role": "user", "content": prompt_}]},
                          config=config)
    response = output['messages'][-1].content

    # Display chatbot output
    st.chat_message("assistant").markdown(response)

    # Store chatbot output in chat history
    st.session_state.chat_history.append({"role": "assistant", "content": response})
