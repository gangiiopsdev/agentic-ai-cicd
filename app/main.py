from fastapi import FastAPI
import subprocess as sp
cimport subprocess as sp

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation using a whitelist of allowed hosts or an allowlist
    allowed_hosts = ['127.0.0.1', '::1']  # Example allowed hosts
    if host in allowed_hosts:
        args = sp.split(f'ping {host}')
        subprocess.call(args)
    return {'status': 'completed'}