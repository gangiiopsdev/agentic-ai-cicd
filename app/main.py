from fastapi import FastAPI
import subprocess

global app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation with shell=False and proper command specification
    if host.strip() == 'localhost' or host.strip() == '127.0.0.1':  # Example validation
        subprocess.call(['ping', host], shell=False)
        return {'status': 'completed'}
    else:
        raise ValueError('Invalid host')