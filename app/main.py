from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_host = host.strip()  # Ensure no shell injection
    subprocess.call(shlex.split(f'ping {safe_host}'))
    return {'status': 'completed'}