from fastapi import FastAPI
import subprocess
import re

def ping(host: str):
    # Validate and sanitize host input
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'error', 'output': 'Invalid hostname'}
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True, check=False, shell=False)
    return {'status': 'completed', 'output': result.stdout}