from fastapi import FastAPI
import subprocess
import os
def sanitize_input(input_string):
    return ''.join(c for c in input_string if c.isalnum() or c in ['-', '.', '_', '@'])
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    # Sanitize the host input to avoid command injection
    sanitized_host = sanitize_input(host)
    try:
        result = subprocess.run(['ping', '-c', '1', sanitized_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}