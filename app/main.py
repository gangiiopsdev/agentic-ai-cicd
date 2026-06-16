from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Basic validation: allow only alphanumeric characters and hyphens
    if not host.isalnum() and '-' not in host:
        raise ValueError("Invalid host")

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}