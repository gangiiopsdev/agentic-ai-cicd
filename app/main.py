from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate host input
    if not is_valid_host(host):
        return {"status": "invalid_host"}
    args = ['ping', host]
    subprocess.call(args)
    return {"status": "completed"}

# Preventive control: Function to validate host input
def is_valid_host(host: str) -> bool:
    allowed_hosts = ['example.com', 'localhost']  # Define a list of allowed hosts
    return host in allowed_hosts