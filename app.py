import streamlit as st
import openai
from langchain.embeddings import OpenAIEmbeddings
from langchain.document_loaders import UnstructuredFileLoader
from store import store_docs
from db_ingester.processor import process_docs
from chat import chat
from utils import StreamHandler, save_file

import os

class FileQaApp:
    def __init__(self):
        self.openai_key = None
        self.uploaded_files = None
        self.store = None

    @st.spinner("Loading files...")
    def load_files(self, uploaded_files):
        files = []
        for file in uploaded_files:
            if file is not None:
                file = save_file(file)
                loader = UnstructuredFileLoader(file)
                os.remove(file)
                files += loader.load()
        
        return files

    @st.spinner("Processing files...")
    def prepare_docs(self, files, embedding_function):
        st.success('Processing uploaded files...')
        processed_docs = process_docs(files)
        st.success('Files processed!')
        st.success('Storing docs!')

        openai.api_key = self.openai_key
        store = store_docs(processed_docs, embedding_function)

        st.success('Docs stored!')
        st.success("Let's talk with your docs.")
        return store

    def main(self):
        st.title("📝 File Q&A with OpenAI")

        with st.sidebar:
            self.openai_api_key = st.text_input("OpenAi API Key", key="file_qa_api_key", type="password")
            self.uploaded_files = st.file_uploader("Choose 1 or more files.", accept_multiple_files=True,
                                                  type=["pdf", "docx", "html", 'txt', 'md', 'json', 'xml'])

        if self.store:
            pass

        elif not self.store and self.uploaded_files and len(self.uploaded_files) > 0:
            st.success("Files uploaded!")

            if st.button("Process Files", key="process_files"):
                if not self.openai_key:
                    if self.openai_api_key:
                        st.session_state.openai_api_key = self.openai_key = self.openai_api_key
                    else:
                        st.warning("Please enter your OpenAI API Key.")
                        return

                embeddings = OpenAIEmbeddings(openai_api_key=self.openai_key)
                files = self.load_files(self.uploaded_files)
                st.session_state.store = self.store = self.prepare_docs(files, embeddings)

        # Store LLM generated responses
        if "messages" not in st.session_state.keys():
            st.session_state.messages = []

        # Display chat messages
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.write(message["content"])

        answer_container = st.container()

        if query:= st.chat_input("Ask question related to your doc/s.", key="query"):
            st.session_state.messages.append({"role": "user", "content": query})
            with st.chat_message("user"):
                st.write(query)

            if st.session_state.messages[-1]["role"] != "Doc Chat":
                with st.chat_message("Doc Chat"):
                    # with st.spinner("Thinking..."):
                    chain = chat(query, self.store, self.openai_key)

                    answer_box = answer_container.empty()

                    print('query: ', query)
                    
                    stream_handler = StreamHandler(st.empty())
                    answer = chain(query, callbacks=[stream_handler])
                    # print('answer: ', answer)
                    st.session_state.messages.append({"role": "Doc Chat", "content": answer['answer']})
        else:
            st.write("Upload files to get started")

if __name__ == "__main__":
    app = FileQaApp()
    st.set_page_config(page_title="🤗💬 DocChat")
    if 'openai_api_key' in st.session_state.keys():
        app.openai_key = st.session_state.openai_api_key

    if 'store' in st.session_state.keys():
        app.store = st.session_state.store

    app.main()
