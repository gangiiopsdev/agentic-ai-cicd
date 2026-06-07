from fastapi import FastAPI
import requests

app = FastAPI()

def ping(host: str):
    try:
        response = requests.get(f'http://{host}/ping', timeout=5)
        return {'status': 'completed', 'output': response.text}
    except requests.RequestException as e:
        return {'status': 'error', 'output': str(e)}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return ping(host)