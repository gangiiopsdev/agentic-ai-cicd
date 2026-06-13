from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation with validation
    allowed_hosts = ['127.0.0.1', '::1']  # Example list of allowed hosts
    if host in allowed_hosts:
        subprocess.call(['ping', host])
        return {'status': 'completed'}
    else:
        return {'status': 'invalid_host'}, 400