from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    args = shlex.split(f'ping {host}')
    return {'status': 'completed'}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)