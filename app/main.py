from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def ping(host: str):
    # Validate host input to prevent injection attacks
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'error', 'output': 'Invalid hostname'}

    # Safe implementation using subprocess.run with shell=False and executable=None
    result = subprocess.run(['ping', '-c 4', host], capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}