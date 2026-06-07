from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate and sanitize the host input
    if not all(c.isalnum() or c in ['.', '-', '_'] for c in host):
        raise ValueError("Invalid host")
    # Secure implementation using subprocess.run
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)