from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

# Replace with your actual Modash API key
API_KEY = "UaxcWljkGvMdnvCLzrar2kR7s2guLm3a"

MODASH_BASE_URL = "https://api.modash.io/v1/influencer"

@app.get("/fetch_influencer_data/")
def fetch_influencer_data(handle: str, platform: str):
    """Fetch influencer data from Modash API."""
    
    url = f"{MODASH_BASE_URL}/{platform}/{handle}"
    headers = {"Authorization": f"Bearer {API_KEY}"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.json(), "status_code": response.status_code}
