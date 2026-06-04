from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Fixed implementation with improved security checks
    if not host.isalnum() or '.' in host:
        raise ValueError('Invalid host')
    subprocess.run(['ping', host], check=True, capture_output=True)

@app.get("/ping")
def ping_route(host: str):
    return await ping(host)