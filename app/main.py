from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the input to avoid command injection
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    command = ['ping', shlex.quote(host)]
    subprocess.call(command)
    return {'status': 'completed'}