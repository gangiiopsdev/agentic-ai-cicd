from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    safe_hosts = ['example.com', 'localhost']
    return host in safe_hosts

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        raise ValueError("Invalid host")
    subprocess.run(['ping', host], check=True, timeout=10)
    return {"status": "completed"}