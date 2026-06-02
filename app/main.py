from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation with validation
    if not host.isalnum() or '.' in host:
        return {'status': 'invalid host'}
    subprocess.call(['ping', host])
    return {'status': 'completed'}