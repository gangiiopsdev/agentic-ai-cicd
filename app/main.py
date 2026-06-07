from fastapi import FastAPI
import subprocess
import os

app = FastAPI()

def validate_host(host):
    # Add validation logic here (e.g., whitelist of allowed hosts)
    return host in ['example.com', 'localhost']

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise ValueError("Invalid host")
    executable_path = "/bin/ping"
    subprocess.run([executable_path, host], check=True, capture_output=True)
    return {"status": "completed"}