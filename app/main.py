from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation using subprocess.run with proper sanitization
    if host.strip() != host or '/' in host:
        raise ValueError('Invalid input for host')
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}