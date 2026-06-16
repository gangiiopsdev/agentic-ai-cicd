from fastapi import FastAPI
import subprocess
cimport socket

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        ipaddress.ip_address(host)
        result = subprocess.call(['ping', host], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    except ValueError:
        return {"error": "Invalid IP address"}

    if result == 0:
        return {"status": "completed", "message": "Ping successful"}
    else:
        return {"status": "failed", "message": "Ping failed"}