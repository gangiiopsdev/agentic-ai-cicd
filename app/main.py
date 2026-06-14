from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation using subprocess.run with input validation
    if not host.isalnum() and not '.' in host:
        raise ValueError('Invalid host parameter')
    args = ['ping', host]
    subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed'}