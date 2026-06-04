from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate the input to prevent command injection
    if not host.isalnum() or not host.startswith('.') and not host.count(':') == 1:
        return {'error': 'Invalid host'}
    subprocess.run(['ping', host], check=True, shell=False)
    return {'status': 'completed'}