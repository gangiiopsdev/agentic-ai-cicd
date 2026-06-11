from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    return host.isalnum() and len(host) <= 15

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        raise ValueError('Invalid host name')
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}