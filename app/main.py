from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation with input validation
    if not host or len(host) > 255:
        raise ValueError('Invalid host parameter')
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {'status': 'completed'}