from fastapi import FastAPI
import subprocess
import os
def safe_ping(host: str):
    # Validate host input
    if not host.isalnum():
        raise ValueError('Invalid host name')
    # Use shell=False and avoid partial paths
    subprocess.run(['ping', host], check=True, shell=False)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if os.path.exists('/sbin/ping'):
        safe_ping(host)
    else:
        raise Exception('Ping executable not found')
    return {'status': 'completed'}