from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if not host.isalnum() or ' ' in host:
        return {'error': 'Invalid hostname'}
    command = ['ping', host]
    result = subprocess.run(command, check=True, shell=False)
    return {'status': 'completed'}