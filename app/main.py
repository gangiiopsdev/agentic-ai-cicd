from fastapi import FastAPI
import subprocess
import os

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if host not in ['allowed_host1', 'allowed_host2']:  # Replace with actual allowed hosts
        raise Exception("Invalid host")
    subprocess.call(['ping', '-c', '1', host])  # Use safe command-line arguments
    return {"status": "completed"}