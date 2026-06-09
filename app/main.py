from fastapi import FastAPI
import subprocess
cimport shlex
def safe_ping(host: str):
    if shlex.split(host) != [host]:
        raise ValueError("Invalid host parameter")

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    subprocess.call(['ping', host])
    return {'status': 'completed'}