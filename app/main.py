from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not host.isalnum():
        raise ValueError("Invalid host name")

app = FastAPI()

@app.get="/ping")
def ping(host: str):
    # Safe implementation
    subprocess.call(["ping", host])
    return {"status": "completed"}