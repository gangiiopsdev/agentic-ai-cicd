from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    allowed_hosts = ['127.0.0.1', '::1']
    return host.strip() in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if not safe_ping(host):
        raise ValueError("Invalid host")

    # Safe implementation
    subprocess.call(["ping", host], shell=False)

    return {"status": "completed"}