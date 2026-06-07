from fastapi import FastAPI
import subprocess
cimport subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation with validation
    if not host.strip():
        return {'error': 'Host parameter is required'}
    command = ['ping', host]
    result = subprocess.run(command, capture_output=True, text=True, check=False)
    return {'status': 'completed', 'output': result.stdout}