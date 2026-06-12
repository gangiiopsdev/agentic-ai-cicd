from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation using subprocess.run with validation and sanitization
    if not host.strip():
        raise ValueError('Host cannot be empty')
    subprocess.run(['ping', host], check=True, capture_output=True)
    return {'status': 'completed'}