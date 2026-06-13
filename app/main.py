from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        ipaddress.ip_address(host)
        return True
    except ValueError:
        return False

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        subprocess.run(["ping", host], check=True)
        return {"status": "completed"}
    else:
        return {"error": "Invalid IP address"}