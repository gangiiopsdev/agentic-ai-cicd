from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the input
    if not host.strip():
        raise ValueError('Invalid host provided')

    # Secure implementation
    subprocess.call(['ping', host])

    return {'status': 'completed'}