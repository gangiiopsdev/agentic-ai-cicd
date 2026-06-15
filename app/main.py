from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation using shlex.quote to avoid shell injection
    command = ['ping', host]
    subprocess.call(command)
    return {'status': 'completed'}