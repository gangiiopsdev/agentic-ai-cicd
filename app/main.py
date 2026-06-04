from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if host.strip() and host.isalnum():
        subprocess.call(['ping', host])
    else:
        raise ValueError('Invalid input for host parameter')
    return {'status': 'completed'}