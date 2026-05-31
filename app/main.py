from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation using a list instead of shell=True and validating input
    if host.strip() == '' or not all(c.isalnum() or c in ['-', '.'] for c in host):
        return {'status': 'error', 'message': 'Invalid hostname'}
    subprocess.call(['ping', host])
    return {'status': 'completed'}