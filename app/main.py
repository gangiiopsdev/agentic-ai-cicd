from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation with input validation
    if host.startswith('.') or host.endswith('.'):  # Example of simple validation
        return {'status': 'invalid_host'}
    subprocess.call(['ping', host])
    return {'status': 'completed'}