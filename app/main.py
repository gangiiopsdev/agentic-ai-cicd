from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation with validation and sanitization
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid input'}
    command = ['ping', host]
    subprocess.run(command, check=True, shell=False)
    return {'status': 'completed'}