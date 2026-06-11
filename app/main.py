from fastapi import FastAPI
import subprocess

def ping(host: str):
    # Validate and sanitize the input
    if not host.strip():
        return {'status': 'failed', 'error': 'Invalid host provided'}
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}