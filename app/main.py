from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize host parameter
    if not host or len(host) > 255:
        raise ValueError('Invalid host parameter')

    # Sanitize the host parameter to prevent shell injection
    sanitized_host = ''.join(c for c in host if c.isalnum() or c in '.-:/')

    subprocess.run(['ping', sanitized_host], check=True)
    return {'status': 'completed'}