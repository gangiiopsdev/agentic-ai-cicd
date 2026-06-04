from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError("Invalid host")
    # Secure implementation using subprocess.run with shell=False
    subprocess.run(["ping", host], check=True)
    return {"status": "completed"}