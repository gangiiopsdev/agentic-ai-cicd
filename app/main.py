from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not host.isalnum() or len(host) > 255:
        raise ValueError('Invalid input for host')
    subprocess.call(['ping', quote(host)])
    return {'status': 'completed'}