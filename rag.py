from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec
from sentence_transformers import SentenceTransformer
from langchain.tools import tool
from dotenv import load_dotenv
import os
from time import sleep
load_dotenv()
api_key = os.getenv("PINECONE_API_KEY")

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

chunks_input = 0

pc = Pinecone(api_key=api_key)

index_name = "standard-dense-py"

if not pc.has_index(index_name):
    pc.create_index(
        name=index_name,
        vector_type="dense",
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        ),
        deletion_protection="disabled",
        tags={
            "environment": "development"
        }
    )

dense_index = pc.Index(index_name)

def upsert_txtpdf(path_txtpdf: str):
    global chunks_input
    lines = open(path_txtpdf, 'r').readlines()
    lines_vectors = model.encode(lines)
    chunks = [{'id': f"{chunks_input + i + 1}", 'values': lines_vectors[i].tolist(), 'metadata':{'text':lines[i]}} for i in range(len(lines))]
    chunks_input += len(lines)
    dense_index.upsert(namespace="the-only-namespace-there-is",vectors=chunks)
    sleep(10)

def delete_index():
    global index_name
    pc.delete_index(index_name)

@tool(description="A tool to query the documents uploaded by the user.")
def query_index(query: str):
    result = dense_index.query(
        namespace="the-only-namespace-there-is",
        vector=model.encode([query])[0].tolist(), 
        top_k=3,
        include_metadata=True,
        include_values=False
    )
    result = " ".join([item['metadata']['text'] for item in result['matches']]) 
    return result


