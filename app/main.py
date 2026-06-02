from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host: str):
    # Basic validation of the host
    if not host.strip().isdigit():
        raise ValueError("Invalid host")

def ping(host: str):
    # Secure implementation with input validation
    subprocess.run(["ping", host], check=True, capture_output=True)

@app.get("/ping")
def ping_endpoint(host: str):
    validate_host(host)
    result = ping(host)
    return {"status": "completed", "output": result.stdout.decode()}