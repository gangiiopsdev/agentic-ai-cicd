from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not host.isalnum() or len(host) > 20:
        raise ValueError('Invalid host input')
    args = ['ping', '-c', '4'] + shlex.split(host)
    subprocess.run(args, check=True, shell=False)
    return {'status': 'completed'}