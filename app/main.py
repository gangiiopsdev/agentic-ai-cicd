from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Use subprocess.run instead of subprocess.call and validate input
    if host and host.isalnum():
        subprocess.run(['ping', host], capture_output=True, text=True)
    else:
        raise ValueError('Invalid host name')

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}