from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation
    subprocess.call(['ping', host])
@app.get("/ping")
def ping_endpoint(host: str):
    # Validate input before using it in subprocess
    if not host.strip():
        raise ValueError("Invalid input")
    return ping(host)