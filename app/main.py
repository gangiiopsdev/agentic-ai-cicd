from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize host input
    if not host.isalnum():
        return {'error': 'Invalid host'}
    # Secure implementation
    subprocess.call(['ping', host], shell=False)
    return {'status': 'completed'}