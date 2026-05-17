import json
import os

CATALOG_PATH = "data/shl_product_catalog.json"

def load_catalog():
    if not os.path.exists(CATALOG_PATH):
        return []

    with open(CATALOG_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    if isinstance(data, list):
        items = data
    elif isinstance(data, dict):
        items = next((v for v in data.values() if isinstance(v, list)), [])
    else:
        items = []

    normalized = []
    for item in items:
        normalized.append({
            "name": item.get("name") or item.get("title") or "Unknown Assessment",
            "url": item.get("url") or item.get("link") or "",
            "description": item.get("description") or item.get("summary") or "",
            "test_type": item.get("test_type") or item.get("type") or "U",
            "raw": item
        })
    return normalized
