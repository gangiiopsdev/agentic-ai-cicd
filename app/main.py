from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate and sanitize the host input to prevent command injection
    if not host.isalnum():
        raise ValueError("Invalid host")
    # Secure implementation using subprocess.run instead of subprocess.call
    subprocess.run(['ping', host], check=True)

@app.get="/ping")
def ping_endpoint(host: str):
    return ping(host)