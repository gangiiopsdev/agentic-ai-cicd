from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the host input
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid hostname'}
    # Secure implementation using subprocess.run
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}