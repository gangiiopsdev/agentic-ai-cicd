from fastapi import FastAPI
import subprocess
import ipaddress

app = FastAPI()

def sanitize_input(value):
    try:
        ipaddress.ip_address(value)
        return True
    except ValueError:
        return False

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not sanitize_input(host):
        return {"error": "Invalid IP address"}, 400
    args = ['ping', host]
    subprocess.run(args, check=True, capture_output=True)
    return {"status": "completed"}