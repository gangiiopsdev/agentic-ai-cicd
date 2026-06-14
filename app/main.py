from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if not host.isalnum() and not any(char in host for char in ['.', '-']):
        raise ValueError('Invalid hostname')
    subprocess.call(['ping', host], shell=False)
    return {'status': 'completed'}