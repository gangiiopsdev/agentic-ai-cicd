from fastapi import FastAPI
import subprocess
from shlex import quote
def is_valid_host(host: str) -> bool:
    # Basic validation to ensure the host contains only valid characters
    return all(c.isalnum() or c in '.-[]' for c in host)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {'error': 'Invalid host'}
    sanitized_host = quote(host, safe='.-[]')  # Sanitize the host to prevent shell injection
    result = subprocess.run(['ping', '-c', '1', sanitized_host], capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}