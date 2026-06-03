from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if not host.isnumeric() or '.' not in host:
        raise ValueError('Invalid host address')
    subprocess.run(['ping', host], check=True)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}