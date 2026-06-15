from fastapi import FastAPI
cimport os
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize the input to prevent command injection
    if not host.isalnum() or len(host) > 255:
        return {'error': 'Invalid host'}, 400
    command = ['ping', host]
    subprocess.call(command)
    return {'status': 'completed'}