import os
import logging
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

data_path = "data/"
faiss_path = "vectorstores/db_faiss"

# Set up logging
logging.basicConfig(level=logging.INFO)

def create_vector_db():
    if not os.path.exists(data_path):
        logging.error(f"Data directory '{data_path}' does not exist.")
        return

    logging.info(f"Loading PDF documents from {data_path}")
    loader = DirectoryLoader(data_path, glob="*.pdf", loader_cls=PyPDFLoader)
    documents = loader.load()

    logging.info(f"Splitting documents into chunks")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    texts = text_splitter.split_documents(documents)

    logging.info(f"Creating embeddings")
    embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2',
                                      model_kwargs={'device': 'cpu'})

    logging.info(f"Creating FAISS vector store")
    db = FAISS.from_documents(texts, embedding)

    logging.info(f"Saving FAISS vector store to {faiss_path}")
    db.save_local(faiss_path)

    logging.info("Vector store creation completed successfully.")


if __name__ == '__main__':
    create_vector_db()
