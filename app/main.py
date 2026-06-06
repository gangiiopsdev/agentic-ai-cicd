from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation using subprocess.run with shell=False
    if not host.isalnum():  # Add validation to ensure the input is safe
        raise ValueError('Invalid input')
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}