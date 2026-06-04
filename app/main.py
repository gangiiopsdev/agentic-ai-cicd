from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not host.isalnum() or host.startswith('-'):
        return {'error': 'Invalid input'}, 400
    command = ['ping', host]
    result = subprocess.run(command, capture_output=True, text=True)
    return {'status': result.stdout}