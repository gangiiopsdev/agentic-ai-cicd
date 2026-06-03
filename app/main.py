from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the host to ensure it contains only allowed characters
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'error': 'Invalid host'}, 400
    subprocess.run(['ping', host], check=True, capture_output=True)
    return {'status': 'completed'}