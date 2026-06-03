from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if host.isnumeric() and len(host) <= 3:
        subprocess.call(['ping', host])
    else:
        raise ValueError('Invalid host input')
    return {'status': 'completed'}