# 🧠 Knowledgebase Creator

AI-powered chatbot knowledgebase creator — Build intelligent chatbots by ingesting your documents and enabling conversational interactions.

## 🚀 Overview

Knowledgebase Creator is a full-stack application that allows users to:

-   📄 **Ingest Documents:** Upload and process various document formats.
-   🧠 **Generate Embeddings:** Convert documents into vector representations using LangChain.
-   💬 **Conversational Interface:** Interact with the ingested knowledgebase through a chatbot interface.

Built with a microservices architecture, the project integrates:

-   **Frontend:** Streamlit
-   **Backend:** FastAPI
-   **AI Capabilities:** LangChain
-   **Data Storage:** ChromaDB
-   **Orchestration:** Docker Compose

## 🧠 Features

-   **Document Ingestion:** Supports uploading and processing of documents.
-   **Vector Embedding:** Utilizes LangChain to generate vector embeddings of the documents.
-   **Knowledgebase Storage:** Stores embeddings in ChromaDB for efficient retrieval.
-   **Chatbot Interface:** Provides a conversational interface to interact with the knowledgebase.

## 🛠️ Tech Stack

-   **Frontend:** Streamlit
-   **Backend:** FastAPI
-   **AI Libraries:** LangChain
-   **Vector Database:** ChromaDB
-   **Containerization:** Docker, Docker Compose
-   **Environment Management:** .env files

## 📦 Installation

1.  **Clone the Repository**

    ```bash
    git clone [https://github.com/Irfan-Ahmad-byte/knowledgebase_creator.git](https://github.com/Irfan-Ahmad-byte/knowledgebase_creator.git)
    cd knowledgebase_creator
    ```

2.  **Set Up Environment Variables**

    Create a `.env` file in the root directory and configure the necessary variables.

3.  **Build and Run with Docker Compose**

    ```bash
    docker-compose up --build
    ```

    The application will be accessible at: `http://localhost:8501`

## 🔍 Usage

1.  **Access the Application**

    Visit `http://localhost:8501` in your browser.

2.  **Upload Documents**

    Use the interface to upload documents you wish to include in the knowledgebase.

3.  **Interact with the Chatbot**

    Engage in conversations with the chatbot to retrieve information from your documents.

## 🧪 Testing

-   **Frontend:** Streamlit's built-in testing capabilities
-   **Backend:** Pytest
-   **API Testing:** Postman or cURL

## 📌 Future Improvements

-   🌐 Support for additional document formats
-   🔐 User Authentication and Authorization
-   🎨 Enhanced UI/UX
-   🚀 Deployment with CI/CD pipelines

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## 📄 License

This project is licensed under the MIT License.

## 👨‍💻 Author

Built with ❤️ by [Irfan Ahmad](!https://github.com/irfan-ahmad-byte)