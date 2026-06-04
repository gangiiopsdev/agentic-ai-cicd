from fastapi import FastAPI
import os
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate the input to prevent command injection
    if not host.isalnum():
        return {'error': 'Invalid host'}
    args = ['ping', f'{host}']
    subprocess.run(args, check=True)
    return {'status': 'completed'}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate the input to prevent command injection
    if not host.isalnum():
        return {'error': 'Invalid host'}
    subprocess.run(['ping', f'{host}'], check=True, shell=False)
    return {'status': 'completed'}