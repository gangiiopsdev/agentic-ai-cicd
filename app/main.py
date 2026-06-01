from fastapi import FastAPI
import subprocess
import os

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(c for c in input_string if c.isalnum() or c in ['-', '.', '_', '@'])

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    full_command = ['ping', sanitized_host]
    try:
        result = subprocess.run(full_command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}