from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not host.isalnum() or len(host) > 255:
        raise ValueError("Invalid host name")
    return host

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    subprocess.call(["ping", safe_ping(host)])
    return {"status": "completed"}