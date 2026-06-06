from fastapi import FastAPI
import re

def ping(host: str):
    # Regular expression to validate hostname
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'error', 'message': 'Invalid hostname'}
    result = subprocess.run(['ping', host], capture_output=True, text=True, shell=False)
    return {'status': 'completed', 'output': result.stdout}