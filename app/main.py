from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the host input using a whitelist approach
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'invalid_host'}
    # Secure implementation
    subprocess.run(['ping', host], check=True, capture_output=True)
    return {'status': 'completed'}