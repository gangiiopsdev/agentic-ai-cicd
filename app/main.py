from fastapi import FastAPI
import subprocess
global_hosts = ['127.0.0.1']

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host in global_hosts:
        subprocess.call(f'ping {host}', shell=False)
    else:
        return {'error': 'Host not allowed'}
    return {'status': 'completed'}