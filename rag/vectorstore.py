from langchain_community.vectorstores import FAISS

def build_vectorstore(chunks, embedding):
    db = FAISS.from_documents(chunks, embedding)
    return db