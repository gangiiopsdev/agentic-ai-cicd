from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Validate and sanitize host input
    allowed_hosts = ['example.com', 'test.com']
    if host in allowed_hosts:
        subprocess.call(["ping", host])
    else:
        raise ValueError('Host not allowed')

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)