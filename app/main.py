from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    args = ['ping', host]
    if not all(arg.isalnum() for arg in args[1:]):
        raise ValueError('Invalid host provided')
    subprocess.call(args)
    return {'status': 'completed'}