from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation
    if not host.isdigit():
        return {'status': 'error', 'message': 'Invalid input'}
    subprocess.call(['ping', host], shell=False)
    return {'status': 'completed'}