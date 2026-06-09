from fastapi import FastAPI
import subprocess
import ipaddress

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        ipaddress.ip_address(host)
    except ValueError:
        return {"error": "Invalid IP address"}, 400
    args = ['ping', host]
    subprocess.run(args, check=True, capture_output=True)
    return {"status": "completed"}