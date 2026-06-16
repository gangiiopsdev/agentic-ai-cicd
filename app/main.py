from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation
    if not host.strip() or '<>' in host:
        raise ValueError('Invalid input for host parameter')
    subprocess.run(['ping', '-c', '4', host], check=True)
    return {'status': 'completed'}