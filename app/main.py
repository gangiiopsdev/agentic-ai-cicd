from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation with input validation
    if host and host.isalnum() and len(host) <= 64:
        subprocess.call(['ping', host])
    else:
        return {'error': 'Invalid host parameter'}
    return {'status': 'completed'}