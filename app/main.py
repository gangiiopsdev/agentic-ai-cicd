from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate and sanitize host input
    if not all(c.isalnum() or c in '._-' for c in host):
        return {'error': 'Invalid host'}
    try:
        result = subprocess.run(['ping', host], check=True, shell=False)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}