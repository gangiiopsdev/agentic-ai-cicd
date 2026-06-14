from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and explicit arguments
    if not re.match(r'^[a-zA-Z0-9]+$', host):
        return {'status': 'error', 'message': 'Invalid hostname'}
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}