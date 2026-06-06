from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation with input sanitization
    if not host.isalnum() or len(host) > 255:
        raise ValueError("Invalid host name")
    safe_host = subprocess.list2cmdline([host])
    subprocess.call(['ping', safe_host])
    return {"status": "completed"}