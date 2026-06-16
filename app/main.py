from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate user input to prevent command injection
    allowed_hosts = ['example.com', 'test.com']  # List of allowed hosts
    if host in allowed_hosts:
        subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed'}
    else:
        raise ValueError('Invalid host')