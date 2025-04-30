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
retriever = vector_store.as_retriever()
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

    llm = ChatOpenAI(model="gpt-4o-mini")
    web_retriever = web_vector_store.as_retriever()
    w_system_prompt = """
        You are an assistant for question-answering tasks.
        Use the following pieces of retrieved context to answer
        the question. If you don't know the answer,  please say 
        "The study material does not contain this information", and then
        use your general knowledge to provide possible answer. In the end,
        please include a sentence to let us know you're using your general knowledge
        to generate response.
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

training_retriever = t_vector_store.as_retriever()
t_system_prompt = """
    You are an assistant for question-answering tasks.
    Use the following pieces of retrieved context to answer
    the question. If you don't know the answer, please say 
    "The study material does not contain this information" , and then
    use your general knowledge to provide possible answer. In the end,
    please include a sentence to let us know you're using your general knowledge
    to generate response.
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
    reference: Annotated[list[str], add]


def resource_rag(state: State):
    url_ans = url_rag_chain.invoke({"input": state['messages'][-1].content})
    if "http" not in url_ans['answer']:
        return {"messages": [AIMessage(content="The resource excel file does not contain relevant information")]}
    url = extract_url(url_ans['answer'])

    web_rag_chain = web_rag(url)
    response = web_rag_chain.invoke({"input": state['messages'][-1].content})
    resource = [doc.metadata['source'] for doc in response['context']]

    return {"messages": [AIMessage(content=response['answer'])],
            "reference": resource}


def training_rag(state: State):
    response = t_rag_chain.invoke({"input": state['messages'][-1].content})
    resource = [doc.metadata['source'] for doc in response['context']]
    return {"messages":[AIMessage(content=response['answer'])],
            "reference": resource}


def summarize(state: State):
    ai_response = []
    for message in reversed(state['messages']):
        if message.type == 'ai':
            ai_response.append(message)
        else:
            break
    ai_response = ai_response[::-1]

    system_message = ("""
        You are a helpful assistant in summarizing. Please summarize the provided AI responses by following
        the below guidelines:
        * Ignore sentences like: "The study material does not provide this information"
        * Include all the main ideas and essential information.
        # Rely strictly on the provided text, without including external information.  
    """)
    prompt = [SystemMessage(content=system_message)] + ai_response
    response = llm.invoke(prompt)

    reference_ls = set(state['reference'])
    reference_text = "\n".join(r for r in reference_ls)
    final_answer = response.content + f"\n\nReferences: \n {reference_text}"
    return {"messages": [AIMessage(content=final_answer)]}


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
