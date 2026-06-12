from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation with shlex.split to safely handle the host input
    subprocess.call(shlex.split(f'ping {host}'))
    return {'status': 'completed'}