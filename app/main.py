from fastapi import FastAPI
import subprocess
cimport = 'ping {}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not host.isalnum():  # Simple validation to prevent shell injection
        raise ValueError('Invalid input')
    command = ['ping', host]
    subprocess.run(command, check=True)
    return {'status': 'completed'}