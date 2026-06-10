from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation using shlex.split to safely split the command into arguments
    subprocess.call(shlex.split('ping ' + host))
    return {'status': 'completed'}