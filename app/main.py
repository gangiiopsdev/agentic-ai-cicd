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
    # Fixed implementation using subprocess.call with shell=False and avoiding command injection
    args = ['ping', host]
    subprocess.run(args, check=True, shell=False)
    return {'status': 'completed'}