from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation with validation and sanitization
    if not host.isalnum():
        return {'status': 'invalid input'}
    subprocess.call(['ping', host])
    return {'status': 'completed'}