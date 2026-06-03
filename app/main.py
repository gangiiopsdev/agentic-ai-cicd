from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation using shlex.quote to safely escape the host parameter
    subprocess.call(f'ping {shlex.quote(host)}', shell=False)
    return {'status': 'completed'}