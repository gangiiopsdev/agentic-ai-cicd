from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        # Secure implementation using subprocess.run with sanitized input
        result = subprocess.run(['ping', '-c', '1', host], check=True, shell=False)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_route(host: str):
    # Sanitize input to prevent injection attacks
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid host'}
    return ping(host)