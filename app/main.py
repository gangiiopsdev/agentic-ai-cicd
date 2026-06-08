from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation
    if host.strip() == '' or any(char in host for char in [';', '&', '|', '`']):
        raise ValueError('Invalid input')
    subprocess.call(['ping', host])
    return {'status': 'completed'}