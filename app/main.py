from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation with input validation and sanitization
    if validate_host(host):
        subprocess.call(['ping', host], shell=False)
        return {'status': 'completed'}
    else:
        return {'status': 'error', 'message': 'Invalid host'}
def validate_host(host: str) -> bool:
    # Add logic to validate the host input
    allowed_hosts = ['example.com', 'test.com']  # Example list of allowed hosts
    return host in allowed_hosts