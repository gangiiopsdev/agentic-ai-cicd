from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate host input using regex to allow only alphanumeric characters, dots, hyphens, and underscores
    if not re.match(r'^[a-zA-Z0-9.-_]+$', host):
        return {'error': 'Invalid host', 'status': 'failed'}
    try:
        subprocess.run(['ping', host], check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        return {'error': str(e), 'status': 'failed'}
    return {'status': 'completed'}