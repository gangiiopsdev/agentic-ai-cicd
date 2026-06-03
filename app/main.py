from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['google.com', 'example.com']  # Define a list of allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    subprocess.run(["ping", host], check=True, shell=False)
    return {"status": "completed"}