from fastapi import FastAPI
import subprocess
import os

app = FastAPI()

def validate_host(host):
    # Basic validation to allow only alphanumeric characters and hyphens
    return all(c.isalnum() or c == '-' for c in host)

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise ValueError('Invalid host')
    command = ["ping", host]
    subprocess.run(command, check=True)
    return {"status": "completed"}