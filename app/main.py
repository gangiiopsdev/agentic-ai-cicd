from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Input validation and sanitization
    if not host.isalnum() or '.' in host:
        return {'error': 'Invalid input'}
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}