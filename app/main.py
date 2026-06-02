from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Input validation for 'host'
    if not host.isalnum() or '.' not in host:
        return {'status': 'error', 'message': 'Invalid input'}
    # Secure implementation with full path and shell=False
    subprocess.call(['/usr/bin/ping', host], shell=False)
    return {'status': 'completed'}