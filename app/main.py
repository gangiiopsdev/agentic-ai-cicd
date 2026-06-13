from fastapi import FastAPI
import subprocess

def ping(host: str):
    # Validate and sanitize host input
    if not isinstance(host, str) or not all(c.isalnum() or c in '.:-' for c in host):
        return {'status': 'error', 'output': 'Invalid host'}
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}