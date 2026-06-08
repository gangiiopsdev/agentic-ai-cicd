from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Define allowed host patterns
    allowed_hosts = re.compile(r'^[a-zA-Z0-9.-]+$')
    if not allowed_hosts.match(host):
        return {"error": "Invalid host"}
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}