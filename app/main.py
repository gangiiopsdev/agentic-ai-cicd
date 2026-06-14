from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize input
    if not host.isalnum():
        return {'error': 'Invalid host name'}
    subprocess.run(['ping', host], check=True, capture_output=True)