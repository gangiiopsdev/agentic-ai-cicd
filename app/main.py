from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the host input
    if not host.isalnum() or len(host) > 100:
        return {'status': 'invalid_host'}

    subprocess.call(['ping', host], shell=False)
    return {'status': 'completed'}