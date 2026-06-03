from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Simple regex to validate host format
    import re
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host)

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise ValueError("Invalid host")
    # Fixed implementation using subprocess.run for better security
    subprocess.run(['ping', host], check=True, shell=False)

    return {"status": "completed"}