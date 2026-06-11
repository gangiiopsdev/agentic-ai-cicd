from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate the host input to prevent shell injection attacks
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {"error": "Invalid hostname"}

    # Secure implementation using subprocess.run with shell=False and args parameter
    subprocess.run(["ping", host], check=True)
    return {"status": "completed"}