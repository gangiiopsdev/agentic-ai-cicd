from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Ensure host is sanitized or validated before use
    allowed_hosts = ['example.com']
    if host not in allowed_hosts:
        raise ValueError('Host not allowed')

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    subprocess.call(["ping", host], shell=False)
    return {"status": "completed"}