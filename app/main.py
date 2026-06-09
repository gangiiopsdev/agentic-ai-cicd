from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Validate and sanitize the host input
    allowed_hosts = ['localhost', '127.0.0.1']
    if host not in allowed_hosts:
        raise ValueError("Invalid host")
    subprocess.call(["ping", host])

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}