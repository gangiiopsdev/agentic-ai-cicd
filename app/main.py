from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation with input validation
    if not host.isalnum():
        return {'status': 'invalid_input'}
    args = ['ping', host]
    subprocess.call(args)
    return {'status': 'completed'}