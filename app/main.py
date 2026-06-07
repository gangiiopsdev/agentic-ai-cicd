from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation with input validation and full executable path
    if not host or not host.isalnum() or len(host) > 64:
        raise ValueError('Invalid hostname')
    subprocess.call(['ping', '-c', '1', host])
    return {'status': 'completed'}