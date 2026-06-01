from fastapi import FastAPI
import subprocess
global_safe_hosts = {'127.0.0.1', '::1'}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host not in global_safe_hosts:
        return {'status': 'error', 'message': 'Invalid host'}
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}