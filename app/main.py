from fastapi import FastAPI
import subprocess

def ping(host: str):
    # Sanitize input
    if not host.isalnum() or '.' not in host:
        return {'status': 'error', 'message': 'Invalid host'}
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}