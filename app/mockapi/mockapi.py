import httpx
import os

def fetch_contacts():
    url = os.getenv("MOCKAPI_URL")
    try:
        with httpx.Client(timeout=5.0) as client:
            response = client.get(url)
            response.raise_for_status()
            return response.json()
    except httpx.RequestError:
        print("❌ Network error")
        return []
    except httpx.HTTPStatusError as exc:
        print(f"❌ Invalid status code: {exc.response.status_code}")
        return []
