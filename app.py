import streamlit as st
import openai
from langchain.embeddings import OpenAIEmbeddings
from langchain.document_loaders import UnstructuredFileLoader
from store import store_docs
from db_ingester.processor import process_docs
from chat import chat
from utils import StreamHandler, save_file

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
                files += loader.load()
        return files

    @st.spinner("Processing files...")
    def prepare_docs(self, files, embedding_function):
        st.markdown('Processing uploaded files...')
        processed_docs = process_docs(files)
        st.markdown('Files processed!')
        st.markdown('Storing docs!')

        openai.api_key = self.openai_key
        store = store_docs(processed_docs, embedding_function)

        st.markdown('Docs stored!')
        st.markdown("Let's talk with your docs.")
        return store

    def main(self):
        st.title("📝 File Q&A with OpenAI")

        with st.sidebar:
            self.openai_api_key = st.text_input("OpenAi API Key", key="file_qa_api_key", type="password")
            self.uploaded_files = st.file_uploader("Choose 1 or more files.", accept_multiple_files=True,
                                                  type=["pdf", "docx", "html", 'txt', 'md', 'json', 'xml'])

        if self.store:
            st.markdown("You already have uploaded files. Let's talk!")

        elif not self.store and self.uploaded_files and len(self.uploaded_files) > 0:
            st.markdown("Files uploaded!")

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

        answer_container = st.container()
        query = st.text_input("Ask questions related to your uploaded files.", key="file_qa_query")

        if query:
            chain, retrieval = chat(query, self.store, self.openai_key)

            answer_box = answer_container.empty()

            print('query: ', query)

            question = f"""You have been provided with a question and related parts from a
                            long text as context, generate a proper answer.

                            question: {query}\n\n

                            context: {retrieval}\n\n

                            Final Answer:
                            
                            """
            
            stream_handler = StreamHandler(answer_box)
            chain.run(question, callbacks=[stream_handler])
        else:
            st.write("Upload files to get started")

if __name__ == "__main__":
    app = FileQaApp()
    try:
        app.openai_key = st.session_state.openai_api_key
    except:
        pass

    try:
        app.store = st.session_state.store
    except:
        pass
    app.main()
