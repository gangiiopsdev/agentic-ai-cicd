from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate input
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid host name'}
    # Secure implementation
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}