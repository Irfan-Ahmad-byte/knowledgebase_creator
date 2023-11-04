from langchain.chains import ConversationChain
from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate, ChatPromptTemplate
from langchain.prompts import MessagesPlaceholder
from langchain.prompts.prompt import PromptTemplate
from langchain.memory import ConversationBufferWindowMemory

from langchain.chains.qa_with_sources.stuff_prompt import PROMPT

def chat(question, store: Chroma, open_ai_api_key: str):
    '''
        function to chat with the chatbot

        parameters:
            question: str: question to ask the chatbot
            store: vector store object

        returns:
            answer: str: answer to the question
    '''
    #get answer from vector store
    retriever = store.as_retriever(search_type='similarity')
    answer = retriever.get_relevant_documents(question)

    llm = ChatOpenAI(
        openai_api_key=open_ai_api_key,
        streaming=True,
        callbacks=[StreamingStdOutCallbackHandler()]
    )

    #load conversation chain
    chain = ConversationChain(
        llm=llm,
        callbacks=[StreamingStdOutCallbackHandler()],
    )

    return chain, answer