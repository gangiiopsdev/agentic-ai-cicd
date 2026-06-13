from fastapi import FastAPI
import subprocess
g import os

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if host not in ('localhost', '127.0.0.1', '::1'):
        raise Exception('Invalid host for security reasons')
    args = ['ping', host]
    subprocess.call(args)
    return {'status': 'completed'}