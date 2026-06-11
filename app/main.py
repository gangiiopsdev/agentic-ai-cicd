from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def ping(host: str):
    # Validate and sanitize input
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'error', 'message': 'Invalid hostname'}
    # Secure implementation using subprocess.run with shell=False and proper argument passing
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}