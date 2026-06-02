from fastapi import FastAPI
import subprocess
global allow_hosts = ['127.0.0.1', 'localhost']

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host in allow_hosts:
        subprocess.call(['ping', host])
    else:
        raise ValueError('Invalid host')
    return {'status': 'completed'}