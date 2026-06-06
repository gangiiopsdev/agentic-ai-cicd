from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation using shlex to safely quote arguments
    import shlex
    command = ['ping', shlex.quote(host)]
    subprocess.call(command)
    return {'status': 'completed'}