from fastapi import FastAPI
import subprocess
import shlex
def sanitize_host(host):
    return shlex.quote(host)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    args = ['ping', sanitized_host]
    subprocess.call(args)
    return {'status': 'completed'}