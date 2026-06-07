from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    allowed_hosts = ["127.0.0.1", "localhost"]
    if host in allowed_hosts:
        subprocess.call(["ping", host])
    else:
        raise ValueError("Host not allowed")

@app.get="/ping")
def ping(host: str):
    return safe_ping(host)