from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation with input validation
    if not host:
        raise ValueError('Host parameter is required')
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {'status': 'completed'}