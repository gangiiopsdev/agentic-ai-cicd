from fastapi import FastAPI
import subprocess
global allowed_hosts = {'example.com'}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host in allowed_hosts:
        subprocess.call(['ping', host])
    else:
        raise ValueError('Host not allowed')
    return {'status': 'completed'}