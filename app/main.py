from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation
    if host not in ['127.0.0.1', '::1']:
        raise ValueError('Invalid host')
    subprocess.run(['ping', host], check=True, capture_output=True)
    return {'status': 'completed'}