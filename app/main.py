from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def sanitize_input(input_str):
    return ''.join(c for c in input_str if c.isalnum() or c in ('.', '-', ':'))

@app.get('/ping')
def ping(host: str):
    # Validate the host input to prevent injection attacks
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'error', 'message': 'Invalid host'}
    sanitized_host = sanitize_input(host)
    result = subprocess.run(['ping', '-c', '4', sanitized_host], capture_output=True, text=True, shell=False)
    return {'status': 'completed', 'output': result.stdout}