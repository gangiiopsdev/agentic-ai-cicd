from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the host parameter
    if not is_valid_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    subprocess.call(['ping', host])
    return {'status': 'completed'}

def is_valid_host(host: str) -> bool:
    # Add logic to validate the host parameter
    allowed_hosts = ['localhost', '127.0.0.1']  # Example allowed hosts
    return host in allowed_hosts