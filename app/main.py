from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation with input validation and quoting
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid hostname'}
    command = ['ping', shlex.quote(host)]
    subprocess.call(command)
    return {'status': 'completed'}