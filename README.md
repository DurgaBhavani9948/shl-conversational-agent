# SHL Conversational Assessment Recommender

## Setup
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
# venv\Scripts\activate  # Windows

pip install -r requirements.txt
python scripts/download_catalog.py
uvicorn app.main:app --reload
```

## Endpoints
- GET /health
- POST /chat

## API Docs
http://127.0.0.1:8000/docs
