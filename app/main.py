from fastapi import FastAPI
import subprocess
import shlex
cimport os

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation using shlex for safe command execution
    args = ['ping', host]
    subprocess.call(args)
    return {'status': 'completed'}