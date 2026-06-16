from fastapi import FastAPI
import subprocess
from typing import List

def ping(host: str):
    # Secure implementation
    try:
        result = subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)
        return {'host': host, 'result': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'host': host, 'error': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    try:
        result = subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)
        return {'host': host, 'result': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'host': host, 'error': str(e)}