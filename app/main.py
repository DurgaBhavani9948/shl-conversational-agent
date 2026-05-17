from fastapi import FastAPI
from .schemas import ChatRequest, ChatResponse
from .catalog_loader import load_catalog
from .retriever import CatalogRetriever
from .agent import ChatAgent

app = FastAPI(title="SHL Conversational Assessment Recommender")

catalog = load_catalog()
retriever = CatalogRetriever(catalog)
agent = ChatAgent(retriever)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    return agent.process(request.messages)
