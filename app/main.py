from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    safe_hosts = ['example.com', 'test.com']  # Replace with actual allowed hosts
    return host in safe_hosts

@app.get("/ping")
def ping(host: str):
    if is_safe_host(host):
        subprocess.run(["ping", host], check=True)
        return {"status": "completed"}
    else:
        raise ValueError("Invalid host")