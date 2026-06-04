from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation
    if not host.isdigit() or len(host) != 3:
        raise ValueError('Invalid host')
    subprocess.call(['ping', host], shell=False)
    return {'status': 'completed'}