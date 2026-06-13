from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Validate and sanitize the host input
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    args = ['ping', host]
    subprocess.call(args)

@app.get("/ping")
def ping(host: str):
    # Safe implementation with validation
    safe_ping(host)
    return {"status": "completed"}