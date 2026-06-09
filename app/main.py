from fastapi import FastAPI
import subprocess
from shlex import quote
import os

app = FastAPI()

def sanitize_input(input_str):
    # Add your sanitization logic here
    return input_str.strip()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    host = sanitize_input(host)
    if not os.path.exists(f'/usr/bin/ping'):  # Check for the existence of the executable
        return {'status': 'error', 'message': 'Ping utility is not available'}
    subprocess.call(['ping', quote(host)])
    return {'status': 'completed'}