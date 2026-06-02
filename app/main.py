from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using subprocess.run
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping(host: str):
    if not valid_host(host):
        raise ValueError("Invalid host")
    safe_ping(host)
    return {"status": "completed"}

def valid_host(host: str) -> bool:
    # Add logic to validate the host input
    allowed_hosts = ["example.com", "localhost"]
    return host in allowed_hosts