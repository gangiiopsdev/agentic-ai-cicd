from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the input
    if not host or len(host) > 255:
        raise ValueError('Invalid host parameter')
    args = ['ping', '--'] + [host]
    subprocess.call(args)
    return {'status': 'completed'}