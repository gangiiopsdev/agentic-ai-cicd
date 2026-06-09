from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    args = ['ping', host]
    subprocess.run(args, check=True, capture_output=True)
    return {'status': 'completed'}