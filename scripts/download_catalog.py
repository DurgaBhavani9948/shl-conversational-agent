import os
import requests

URL = "https://tcp-us-prod-rnd.shl.com/voiceRater/shl-ai-hiring/shl_product_catalog.json"
OUTPUT_PATH = "data/shl_product_catalog.json"

def main():
    os.makedirs("data", exist_ok=True)
    response = requests.get(URL, timeout=60)
    response.raise_for_status()
    with open(OUTPUT_PATH, "wb") as f:
        f.write(response.content)
    print(f"Saved to {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
