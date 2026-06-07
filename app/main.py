from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if not host.isalnum() or len(host) > 100:
        return {'status': 'error', 'message': 'Invalid host name'}
    subprocess.call(['ping', '-c', '4', host])
    return {'status': 'completed'}