from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation with input validation
    if not host.isalnum() or '@' in host:
        raise ValueError('Invalid host provided')
    args = ['ping', host]
    subprocess.call(args)
    return {'status': 'completed'}