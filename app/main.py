from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not host.isdigit():
        raise ValueError('Invalid host')
    # Safe implementation with input validation and escaping
    subprocess.call(['ping', '-c', '1', host])
    return {'status': 'completed'}