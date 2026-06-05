from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(hostname):
    # Simple validation example: allow only alphanumeric characters and periods
    return hostname.isalnum() or '.' in hostname

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError("Invalid host name")
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}