from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation with validation and escaping
    if host not in ['example.com', 'localhost']:
        return {'status': 'error', 'message': 'Invalid host'}
    subprocess.call(['ping', host])
    return {'status': 'completed'}