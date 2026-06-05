from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation with input validation
    if not host.isalnum() and not '.' in host:
        raise ValueError('Invalid host parameter')
    command = ['ping', host]
    subprocess.run(command, check=True)
    return {'status': 'completed'}