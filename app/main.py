from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation
    if host.startswith('localhost') or host.startswith('127.0.0.1'):
        subprocess.call(['ping', host])
    return {'status': 'completed'}