from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    # Simple validation logic, replace with more robust checks
    return host.isalnum()

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError("Invalid host name")
    # Secure implementation using subprocess.run with shell=False and a list of arguments
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}