from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation
    if '/' not in host and '\' not in host:
        subprocess.call(['ping', host], shell=False)
    else:
        raise ValueError('Invalid hostname')
    return {'status': 'completed'}