from fastapi import FastAPI
import subprocess
import os

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation using platform-independent method
    if host in ['127.0.0.1', '::1']:  # Allow only localhost for simplicity
        subprocess.call(['ping', '-c', '4', host])  # Use -c for number of pings
        return {'status': 'completed'}
    else:
        return {'status': 'denied'}, 403