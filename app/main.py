from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using subprocess.run with shell=False and a list of arguments
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError("Invalid host")
    safe_ping(host)
    return {"status": "completed"}

def is_valid_host(host: str) -> bool:
    # Add validation logic here, e.g., IP address format
    return True