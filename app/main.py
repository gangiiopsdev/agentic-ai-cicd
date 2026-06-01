from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def validate_host(host):
    return bool(re.match(r'^[a-zA-Z0-9.-]+$', host))

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        raise ValueError('Invalid hostname')

    # Safe implementation using subprocess.run with shell=False
    result = subprocess.run(['ping', host], check=True, capture_output=True)
    return {'status': 'completed', 'output': result.stdout.decode()}