from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation with input validation
    if not host.isalnum() and '-' not in host:
        return {'status': 'invalid host'}
    subprocess.call(['ping', host], shell=False)
    return {'status': 'completed'}