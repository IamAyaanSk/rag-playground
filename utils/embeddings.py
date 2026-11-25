import numpy as np
from langchain_openai import OpenAIEmbeddings

embedding_model = OpenAIEmbeddings(
    model="text-embedding-qwen3-embedding-0.6b", check_embedding_ctx_length=False
)


def get_batch_embeddings(docs: list[str]):
    return embedding_model.embed_documents(docs)


def get_embedding(query: str):
    return embedding_model.embed_query(query)


def calculate_similarities(doc_vectors: list[list[float]], query_vector: list[float]):
    cosine_similarity = (
        np.dot(doc_vectors, query_vector)
        / np.linalg.norm(doc_vectors)
        * np.linalg.norm(query_vector)
    )

    return cosine_similarity
