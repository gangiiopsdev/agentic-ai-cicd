from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    # Add logic to check if the host is safe to ping
    return host in ['safe1.example.com', 'safe2.example.com']

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        raise ValueError("Invalid host")
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}