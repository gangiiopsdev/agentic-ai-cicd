from fastapi import FastAPI
import subprocess
cimport netaddr

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    if netaddr.valid_ip(host):
        result = subprocess.call(["ping", host])
    else:
        raise ValueError("Invalid IP address")
    return {"status": "completed"}