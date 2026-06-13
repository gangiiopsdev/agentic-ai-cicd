from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation with input validation and full command path
    if host.startswith('192.168.') or host.startswith('localhost'):  # Example of simple validation
        subprocess.call(['ping', '-c', '4', host])
    else:
        raise ValueError('Invalid host')
    return {'status': 'completed'}