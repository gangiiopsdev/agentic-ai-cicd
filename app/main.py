from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation with input validation
    if not is_valid_host(host):
        raise ValueError("Invalid host")
    subprocess.call(["ping", host])
    return {"status": "completed"}

def is_valid_host(host: str) -> bool:
    # Basic validation to ensure the host is a valid IP address or hostname
    import ipaddress
    try:
        ipaddress.ip_address(host)
    except ValueError:
        return False
    return True