from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation
    if host and host.strip() != 'localhost':
        return {'error': 'Invalid or restricted host'}
    subprocess.call(['ping', host], shell=False)
    return {'status': 'completed'}