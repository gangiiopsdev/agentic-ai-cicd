from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate the host input to ensure it does not contain malicious content
    if not host or len(host) > 255:
        raise ValueError("Invalid host")
    # Secure implementation using subprocess.run instead of shell=True
    subprocess.run(['ping', '-c', '1', host], check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)