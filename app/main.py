from fastapi import FastAPI
import subprocess
import ipaddress

app = FastAPI()

def is_valid_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not is_valid_ip(host):
        return {"status": "failed", "error": "Invalid IP address"}
    try:
        result = subprocess.run(["ping", host], capture_output=True, text=True, timeout=5, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}