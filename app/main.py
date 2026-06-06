from fastapi import FastAPI
import subprocess
import shlex
import ipaddress

app = FastAPI()

def validate_host(host: str) -> bool:
    try:
        ipaddress.ip_address(host)
        return True
    except ValueError:
        return False

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        safe_host = shlex.quote(host)
        subprocess.run(['ping', '-c', '1', safe_host], check=True, capture_output=True)
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}, 400