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
    safe_host = ''.join(ch for ch in host if ch.isalnum() or ch in '-_.')
    args = shlex.split(f'ping {safe_host}')
    subprocess.call(args)
    return {'status': 'completed'}