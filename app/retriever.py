from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

class CatalogRetriever:
    def __init__(self, catalog):
        self.catalog = catalog
        if not catalog:
            self.model = None
            self.index = None
            return

        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        texts = [
            f"{item['name']} {item['description']} {item['test_type']}"
            for item in catalog
        ]
        embeddings = self.model.encode(
            texts, convert_to_numpy=True, show_progress_bar=False
        ).astype("float32")

        self.index = faiss.IndexFlatL2(embeddings.shape[1])
        self.index.add(embeddings)

    def search(self, query, top_k=10):
        if not self.catalog or self.index is None:
            return []

        query_embedding = self.model.encode(
            [query], convert_to_numpy=True
        ).astype("float32")

        k = min(top_k, len(self.catalog))
        _, indices = self.index.search(query_embedding, k)

        return [self.catalog[i] for i in indices[0] if 0 <= i < len(self.catalog)]
