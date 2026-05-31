from fastapi import FastAPI
import subprocess
cimport = subprocess.call

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = host.strip().replace(';', '').replace('&', '')
    cimport(f'ping {sanitized_host}')
    return {'status': 'completed'}