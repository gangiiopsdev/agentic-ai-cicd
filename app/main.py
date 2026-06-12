from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation with input validation
    if not host.isalnum() or len(host) > 255:
        return {'status': 'error', 'message': 'Invalid hostname'}
    subprocess.call(['ping', host])
    return {'status': 'completed'}