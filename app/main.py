from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation
    allowed_hosts = ['google.com', 'example.com']  # Define a list of allowed hosts
    if host in allowed_hosts:
        subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    else:
        return {'error': 'Invalid host'}

    return {'status': 'completed'}