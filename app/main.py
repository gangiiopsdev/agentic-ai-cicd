from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using subprocess.run with shell=False and arguments properly sanitized
    subprocess.run(['ping', host], check=True, capture_output=True, text=True)

@app.get("/ping")
def ping(host: str):
    if not all(c.isalnum() or c in '._-' for c in host):
        raise ValueError('Invalid host name')
    safe_ping(host)
    return {"status": "completed"}