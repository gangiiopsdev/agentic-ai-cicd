from fastapi import FastAPI
import subprocess
import re

def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e in ['.', '-'])

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize the host input to prevent command injection
    sanitized_host = sanitize_input(host)
    if not sanitized_host:
        return {'status': 'error', 'message': 'Invalid host format'}

    # Secure implementation using subprocess.run with shell=False and full executable path
    result = subprocess.run(['ping', '-c', str(1), sanitized_host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}