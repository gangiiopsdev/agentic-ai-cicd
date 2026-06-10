from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Safe implementation using subprocess.run with full path and shell=False
    if not host.strip() or not host.isalnum():
        raise ValueError('Invalid host input')
    result = subprocess.run(['/usr/bin/ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'stdout': result.stdout}