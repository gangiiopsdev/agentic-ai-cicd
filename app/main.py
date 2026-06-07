from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safer implementation using subprocess.run with proper validation
    if host.startswith('127.0.0.1') or host.startswith('localhost'):
        subprocess.run(['ping', host], check=True, capture_output=True)
    else:
        raise ValueError('Invalid host for ping operation')

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)