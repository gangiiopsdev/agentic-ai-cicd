from fastapi import FastAPI
import subprocess
global ALLOWED_HOSTS = ['example.com']

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host in ALLOWED_HOSTS:
        subprocess.run(['ping', host], check=True, capture_output=True, text=True)
    else:
        raise ValueError('Unauthorized host')
    return {'status': 'completed'}