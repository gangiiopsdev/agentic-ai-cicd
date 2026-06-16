from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation
    if host and '-' not in host and len(host) <= 15:
        subprocess.call(['ping', '-c', '4', host])
    return {'status': 'completed'}