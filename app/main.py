from fastapi import FastAPI
import shlex
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_host = shlex.quote(host)
    command = ['ping', safe_host]
    subprocess.call(command)
    return {'status': 'completed'}