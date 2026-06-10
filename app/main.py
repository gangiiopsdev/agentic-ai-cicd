from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if host and '-' not in host:
        subprocess.call(['ping', host], shell=False)
    else:
        raise ValueError('Invalid host parameter')
    return {'status': 'completed'}