from fastapi import FastAPI
import subprocess
import ipaddress

def safe_ping(host: str):
    try:
        ipaddress.ip_address(host)
    except ValueError:
        raise ValueError("Invalid hostname")
    args = ['ping', host]
    result = subprocess.call(args)
    return result

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    status = safe_ping(host)
    return {"status": status}