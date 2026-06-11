from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the input
    if not host.strip() or any(char in host for char in [';', '&', '|', '>', '<', '`']):
        return {'status': 'error', 'message': 'Invalid input'}
    subprocess.call(['ping', host], shell=False)
    return {'status': 'completed'}