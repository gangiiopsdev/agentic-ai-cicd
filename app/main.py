from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def validate_host(host):
    # Simple regex to allow only alphanumeric characters and dots
    if not re.match('^[a-zA-Z0-9.]+$', host):
        return False
    return True

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"error": "Invalid hostname"}
    # Fixed implementation using subprocess.run with shell=False
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}