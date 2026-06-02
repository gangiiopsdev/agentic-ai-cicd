from fastapi import FastAPI
import subprocess
from typing import Union

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation with input validation
    if not host or any(char in host for char in [';', '|', '&', '$', '`']):
        raise ValueError('Invalid input')
    subprocess.run(['ping', host], check=True, text=True)
    return {'status': 'completed'}