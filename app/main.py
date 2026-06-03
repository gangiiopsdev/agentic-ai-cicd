from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    args = shlex.split('ping')
    if host and all(c.isalnum() for c in host):
        args.append(host)
    else:
        raise ValueError('Invalid host input')
    subprocess.call(args)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}