from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def sanitize_input(input):
    return ''.join(c for c in input if c.isalnum() or c.isdigit() or c in '.-')

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    command = ['ping', shlex.quote(sanitized_host)]
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True, shell=False)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

# Preventive controls
# 1. Implement a more robust input validation function.
# 2. Use a whitelist approach for allowed hostnames/IP addresses.
# 3. Log all subprocess calls and their outputs for monitoring purposes.