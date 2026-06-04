from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and quoting user input
    if not host.isalnum() or len(host) > 255:
        raise ValueError('Invalid host name')
    command = ['ping', shlex.quote(host)]
    result = subprocess.run(command, capture_output=True, text=True)
    return {'status': 'completed'}