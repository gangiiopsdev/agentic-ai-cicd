from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate the host input
    if not all(c.isalnum() or c in ['-', '.', '_', ':'] for c in host):
        raise ValueError('Invalid host name')
    # Safe implementation using subprocess.run
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping_route(host: str):
    return ping(host)