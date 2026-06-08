from fastapi import FastAPI
import subprocess
globally_banned_hosts = ['127.0.0.1', '::1']

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host in globally_banned_hosts:
        raise ValueError('Host is not allowed')
    subprocess.run(['ping', '--count=1', host], capture_output=True, text=True)
    return {'status': 'completed'}