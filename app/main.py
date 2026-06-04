from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation with validation
    if not host:
        raise ValueError('Host parameter is required')
    subprocess.call(['ping', '-c', '4', host])  # Use a specific number of pings for security
    return {'status': 'completed'}