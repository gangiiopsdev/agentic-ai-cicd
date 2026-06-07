from fastapi import FastAPI
import os
import subprocess
import shlex

app = FastAPI()

def sanitize_input(input_string):
    return ''.join(e if e.isalnum() else '_' for e in input_string)

@app.get('/ping')
def ping(host: str):
    # Sanitize the host input to avoid command injection
    sanitized_host = sanitize_input(host)
    try:
        result = subprocess.run(['ping', '-c', '1', f'/bin/ping', sanitized_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}