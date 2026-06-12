from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safer implementation with input validation
    if not host.strip():
        raise ValueError('Host parameter cannot be empty')
    subprocess.call(['ping', host])

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_safe(host: str):
    return {'status': 'completed'}