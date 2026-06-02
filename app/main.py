from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['127.0.0.1', '::1']  # Add more valid hosts as needed
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise ValueError("Invalid host")
    # Secure implementation
    subprocess.call(["ping", host], shell=False)
    return {"status": "completed"}