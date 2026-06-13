from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        response = requests.get(f'http://{host}/ping')
        return {'status': 'completed', 'response': response.text}
    except requests.RequestException as e:
        return {'status': 'failed', 'error': str(e)}