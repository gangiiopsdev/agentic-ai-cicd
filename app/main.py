from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation using subprocess.call with shell=False and validating input
    if host.isnumeric() or '.' in host:
        subprocess.run(['ping', host], check=True)
        return {'status': 'completed'}
    else:
        return {'error': 'Invalid host'}, 400