from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate the host input to ensure it does not contain malicious content
    if not host.isalnum():
        raise ValueError('Invalid host input')
    subprocess.call(['ping', host])
    return {'status': 'completed'}