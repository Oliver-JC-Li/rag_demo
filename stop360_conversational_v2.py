from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.history_aware_retriever import create_history_aware_retriever
from langchain.chains.retrieval import create_retrieval_chain
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.messages import HumanMessage, AIMessage
import streamlit as st


openai_api_key = st.secrets["OPENAI_API_KEY"]

# llm = ChatOpenAI(model='gpt-4o-mini', api_key=openai_api_key)

# Load the documents
def get_vector_store(path):
    docs = PyPDFLoader(path).load()
    doc_chunks = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=20).split_documents(docs)
    vector_db = FAISS.from_documents(doc_chunks, embedding=OpenAIEmbeddings())
    return vector_db


# History aware retrieval chain
def get_history_aware_retriever(vector_store):
    llm = ChatOpenAI(model="gpt-4o-mini", api_key=openai_api_key)
    retriever = vector_store.as_retriever()
    history_prompt = """
    Given a chat history and the latest user question which might
    reference context in the chat history, formulate a standalone
    question which can be understood without the chat history. Do
    NOT answer the question, just reformulate it if needed and otherwise
    return it as is.
    """

    prompt = ChatPromptTemplate.from_messages([
        ("system", history_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}")
    ])
    history_aware_chain = create_history_aware_retriever(llm, retriever, prompt)
    return history_aware_chain


# context_q_system_prompt = ("""
# Given a chat history and the latest user question which might
# reference context in the chat history, formulate a standalone
# question which can be understood without the chat history. Do
# NOT answer the question, just reformulate it if needed and otherwise
# return it as is.
# """)

# llm = ChatOpenAI(model='gpt-4o-mini')

# context_q_prompt = ChatPromptTemplate.from_messages(
#     [
#         ("system", context_q_system_prompt),
#         MessagesPlaceholder("chat_history"),
#         ("human", "{input}")
#     ]

# )
# history_aware_retriever = create_history_aware_retriever(llm, retriever, context_q_prompt)

# Question Answering
def get_qa_chain(history_aware_retriever):
    llm = ChatOpenAI(model="gpt-4o-mini", api_key=openai_api_key)
    qa_prompt = """
    You are a nurse to help recruiting participants for STOP360 research study.
    Please answer user question using the below context and explain it in four-grade literacy level. 
    Please try to provide plain-languague reponses succinctly.
    <context>
    {context}
    </context>
    """
    prompt = ChatPromptTemplate.from_messages([
        ("system", qa_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}")
    ])

    qa_chain = create_stuff_documents_chain(llm, prompt)
    qa_rag_chain = create_retrieval_chain(history_aware_retriever, qa_chain)
    return qa_rag_chain

# system_prompt = ("""
# You are an assistant for question-answering tasks. Use the following
# pieces of retrieved context to answer the question.
# <context>
# {context}
# </context>
# """)

# qa_prompt = ChatPromptTemplate.from_messages(
#     [
#         ("system", system_prompt),
#         MessagesPlaceholder("chat_history"),
#         ("human", "{input}")
#     ]
# )
# question_answer_chain = create_stuff_documents_chain(llm, qa_prompt)
# rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)

def get_response(user_input):
    history_chain = get_history_aware_retriever(st.session_state.vector_store)
    qa_chain = get_qa_chain(history_chain)
    response = qa_chain.invoke({
        "chat_history": st.session_state.chat_history,
        "input": user_input
    })
    return response['answer']

# streamlit framework
st.title("Virtual Assistant to answer question regarding STOP360 study")

# Create and store chat history and vector db in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "vector_store" not in st.session_state:
    st.session_state.vector_store = get_vector_store("./stop360/STOP360_Template.pdf")

# Display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Get user input and chatbot response
if prompt_ := st.chat_input("Please ask any question you have regarding ABC problem solving strategy"):

    st.chat_message("user").markdown(prompt_)

    st.session_state.chat_history.append({"role": "user", "content": prompt_})

    response = get_response(prompt_)

    # Display chatbot output
    st.chat_message("assistant").markdown(response)

    # Store chatbot output in chat history
    st.session_state.chat_history.append({"role": "assistant", "content": response})


# Manage chat history
# chat_history = {}


# def get_session_history(session_id: str) -> BaseChatMessageHistory:
#     if session_id not in chat_history:
#         chat_history[session_id] = ChatMessageHistory()
#     return chat_history[session_id]


# conversational_rag_chain = RunnableWithMessageHistory(
#     rag_chain,
#     get_session_history,
#     input_messages_key="input",
#     history_messages_key="chat_history",
#     output_messages_key="answer"
# )

# # Streamlit framework
# vector_store = []
# st.header("STOP360 conversational chatbot")

# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = [
#         AIMessage(content="I am a vertual study assistant, please as any question regarding STOP360 study")
#     ]

# if vector_store not in st.session_state:
#     st.session_state.vector_store = retriever

# user_input = st.chat_input("Ask you question over here")

# if user_input is not None and user_input.strip() != "":
#     response = conversational_rag_chain.invoke(
#         {'input': user_input},
#         config={
#             "configurable": {"session_id": "stop360_1"}
#         }
#     )['answer']

#     st.session_state.chat_history.append(HumanMessage(content=user_input))
#     st.session_state.chat_history.append(AIMessage(content=response))

# for message in st.session_state.chat_history:
#     if isinstance(message, AIMessage):
#         with st.chat_message("AI"):
#             st.write(message.content)
#     else:
#         with st.chat_message("Human"):
#             st.write(message.content)