from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host: str):
    # Basic validation of the host
    allowed_hosts = ['127.0.0.1', '::1']  # Example allowed hosts
    if host not in allowed_hosts:
        raise ValueError("Invalid host")

@app.get("/ping")
def ping_endpoint(host: str):
    validate_host(host)
    result = subprocess.run(["ping", host], check=True, capture_output=True)
    return {"status": "completed", "output": result.stdout.decode()}