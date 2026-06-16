from fastapi import FastAPI
import os
import subprocess

cmd = ['ping', host]

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize the input to prevent command injection
    if not host.isalnum() or len(host) > 255:
        return {'error': 'Invalid host'}, 400
    result = subprocess.run(cmd, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}