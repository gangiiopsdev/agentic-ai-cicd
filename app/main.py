from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not host.isdigit() or len(host) > 15:
        raise ValueError('Invalid host address')
    subprocess.call(['ping', host])
    return {'status': 'completed'}