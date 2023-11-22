from langchain.chains import ConversationChain, ConversationalRetrievalChain
from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate, ChatPromptTemplate
from langchain.prompts import MessagesPlaceholder
from langchain.prompts.prompt import PromptTemplate
from langchain.memory import ConversationBufferWindowMemory

import os
from dotenv import load_dotenv, find_dotenv
from langchain.chat_models import ChatOpenAI, ChatOllama
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chains import RetrievalQA, LLMChain, RetrievalQAWithSourcesChain, ConversationChain
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.memory import ConversationBufferMemory, ConversationBufferWindowMemory
from langchain.prompts import PromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain.vectorstores.chroma import Chroma
from langchain.schema import AIMessage, SystemMessage, HumanMessage
from langchain.callbacks.base import BaseCallbackHandler
from langchain.chains.qa_with_sources import load_qa_with_sources_chain


from langchain.chains.qa_with_sources.stuff_prompt import PROMPT

def chat(store: Chroma, open_ai_api_key: str, role='Analyst', name='DocChat'):
    '''
        function to chat with the chatbot

        parameters:
            question: str: question to ask the chatbot
            store: vector store object

        returns:
            answer: str: answer to the question
    '''

    if not role:
        role = 'Analyst'
    if not name:
        name = 'DocChat'

    system_template =  'You are an ' + role + 'And, your name is ' + name + '''.

    Provided a question and a context summary, give an answer according to the question.

    ####
    Summary: {summary}
    ####

    Answer:
    '''

    # Initialize the ChatOpenAI object with OpenAI API key and model name
    llm = ChatOpenAI(openai_api_key=open_ai_api_key, streaming=True, 
                            callbacks = [StreamingStdOutCallbackHandler()])
    
    memory = ConversationBufferMemory()

    human_message = 'Question: {question}'
        
    messages = [
        SystemMessagePromptTemplate.from_template(system_template),
        HumanMessagePromptTemplate.from_template(human_message)
    ]

    qa_prompt = ChatPromptTemplate.from_messages(messages)

    qa_chain = load_qa_with_sources_chain(
        llm,
        chain_type="stuff",
        prompt=qa_prompt,
    )
    
    chain = RetrievalQAWithSourcesChain(
        combine_documents_chain=qa_chain,
        retriever=store.as_retriever(search_kwargs={"k": 2}),
        memory=memory,
    )

    return chain