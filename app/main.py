from fastapi import FastAPI
import subprocess
from shlex import quote
def safe_ping(host: str):
    cmd = ['ping', host]
    return subprocess.call(cmd)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}