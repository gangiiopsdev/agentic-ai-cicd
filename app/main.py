from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Enhanced validation and sanitization
    if not host.isalnum():
        return {'error': 'Invalid input'}
    args = ['ping', host]
    subprocess.call(args)
    return {'status': 'completed'}