from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation using subprocess.run with input validation
    if not re.match(r'^[a-zA-Z0-9.-]+$', host) or '.' in host:
        return {'status': 'error', 'output': 'Invalid host'}
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}