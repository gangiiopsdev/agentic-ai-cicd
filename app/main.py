from fastapi import FastAPI
import subprocess
from typing import List

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the host input to avoid command injection
    allowed_hosts = ['example.com', 'test.com']  # Define a list of allowed hosts
    if host in allowed_hosts:
        subprocess.call(["ping", host])
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}