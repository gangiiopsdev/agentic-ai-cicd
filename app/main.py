from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation using shlex.split
    cmd = ['ping'] + shlex.split(host)
    subprocess.call(cmd, shell=False)
    return {'status': 'completed'}