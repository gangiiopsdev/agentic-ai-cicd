from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    allowed_hosts = ['127.0.0.1', 'localhost']
    if host in allowed_hosts:
        subprocess.run(['ping', host], check=True)
    else:
        return {'status': 'error', 'message': 'Invalid host'}
    return {'status': 'completed'}