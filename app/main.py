from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation with input validation
    if host.isalnum() and '.' in host:
        command = ['ping', host]
        subprocess.call(command)
    return {'status': 'completed'}