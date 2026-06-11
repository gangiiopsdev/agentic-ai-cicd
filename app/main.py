from fastapi import FastAPI
import subprocess
globally_safe_hosts = ['127.0.0.1', '::1']

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host not in globally_safe_hosts:
        raise ValueError('Untrusted host specified')
    subprocess.call(f'ping {host}')
    return {'status': 'completed'}