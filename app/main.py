from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation using subprocess.run with shell=False and explicit arguments
    if host.isnumeric() or '.' in host:
        subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}