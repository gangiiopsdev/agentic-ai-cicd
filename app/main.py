from fastapi import FastAPI
import subprocess
import re
cimport shlex

app = FastAPI()

def sanitize_host(host):
    # Allow only alphanumeric characters, hyphens, and dots
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(c for c in host if c in allowed_chars)

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    # Use regex to validate the sanitized host for safety
    if not re.match(r'^[a-zA-Z0-9.-]*$', sanitized_host):
        return {'status': 'error', 'message': 'Invalid host'}
    result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}