from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate user input
    if not all(c.isalnum() for c in host):
        raise ValueError('Invalid characters in host name')
    # Secure implementation using subprocess.call with shell=False and args parameter
    subprocess.run(['ping', host], check=True, capture_output=True)
    return {'status': 'completed'}