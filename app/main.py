from fastapi import FastAPI
import requests
def safe_get(url, timeout=5):
    try:
        return requests.get(url, timeout=timeout)
    except requests.RequestException as e:
        return None

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host.startswith('http://') and not host.startswith('https://'):
        return {'status': 'failed', 'error': 'Invalid URL format'}
    url = f'http://{host}/ping'
    response = safe_get(url)
    if response:
        return {"status": "completed", "response": response.text}
    else:
        return {"status": "failed", "error": "Request timed out or failed"}