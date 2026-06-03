from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Fixed implementation
    subprocess.run(['ping', host], check=True, capture_output=True)

@app.get("/ping")
def ping_route(host: str):
    if not host.isalnum() or '.' in host:
        raise ValueError('Invalid host')
    return await ping(host)