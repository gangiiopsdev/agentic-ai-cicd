from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate the host name to prevent command injection
    if not all(c.isalnum() or c in ['-', '.', '_'] for c in host):  # Allow alphanumeric, hyphen, dot, and underscore
        return {'status': 'failed', 'error': 'Invalid host name'}
    try:
        subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    if not host.isalnum():  # Add validation for untrusted input
        return {'status': 'failed', 'error': 'Invalid host name'}
    return ping(host)