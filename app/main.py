from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation using subprocess.run without shell=True and validation
    if not host.strip().isalnum() or len(host) > 255:
        return {'status': 'invalid input'}
    subprocess.call(['ping', host])
    return {'status': 'completed'}