from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize host parameter
    if not host or len(host) > 255:
        raise ValueError('Invalid host parameter')
    sanitized_host = subprocess.list2cmdline([host])
    subprocess.run(['ping', sanitized_host], check=True)
    return {'status': 'completed'}