from fastapi import FastAPI
import subprocess
cimport ipaddress

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        ipaddress.ip_address(host)
        # Safe implementation using subprocess.call without shell=True
        subprocess.call(["ping", host])
    except ValueError:
        return {"status": "Invalid IP address"}
    return {"status": "completed"}