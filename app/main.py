from fastapi import FastAPI
import subprocess
from ipaddress import ip_address

app = FastAPI()

def safe_ping(host):
    try:
        ip_address(host)
        return subprocess.run(['ping', host], capture_output=True, text=True)
    except ValueError:
        raise ValueError('Invalid IP address')

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        result = safe_ping(host)
        return {
            "status": "completed",
            "result": result.stdout,
            "stderr": result.stderr
        }
    except ValueError as e:
        return {"error": str(e)}