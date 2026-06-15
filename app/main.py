from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using subprocess.run with validation
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    subprocess.run(['ping', '--', host], check=True)

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    safe_ping(host)

    return {"status": "completed"}