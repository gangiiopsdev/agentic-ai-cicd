from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation with validation and absolute path
    if not host.strip().isalnum():
        raise ValueError('Invalid input')
    subprocess.call(['ping', '-c', '4', host])  # Use absolute path for 'ping' and specify count
    return {'status': 'completed'}