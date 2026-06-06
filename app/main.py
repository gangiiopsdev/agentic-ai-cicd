from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not is_safe_host(host):
        raise ValueError("Unsafe host")
    args = ['ping', host]
    subprocess.call(args)

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    safe_ping(host)
    return {"status": "completed"}

def is_safe_host(host: str):
    allowed_hosts = ['example.com']  # List of allowed hosts
    return host in allowed_hosts