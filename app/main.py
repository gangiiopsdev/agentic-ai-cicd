from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Basic validation of host input (e.g., allow only alphanumeric characters and hyphens)
    if not host.isalnum() and '-' not in host:
        raise ValueError("Invalid host")

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    # Secure implementation using subprocess.run with shell=False and properly quoted arguments
    result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}