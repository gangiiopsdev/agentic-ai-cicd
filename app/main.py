from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not host.strip().isalnum():
        raise ValueError('Invalid host name')
    subprocess.run(["ping", host], check=True)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    return safe_ping(host)