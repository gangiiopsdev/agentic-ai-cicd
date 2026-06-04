from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    command = 'ping -c 4'
    args = shlex.split(command + ' ' + host)
    subprocess.call(args, shell=False)
    return {'status': 'completed'}