from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if not valid_host(host):
        raise ValueError("Invalid host")
    subprocess.call(['ping', host])

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}

def valid_host(host: str) -> bool:
    # Add validation logic here, e.g., check if the host is in a whitelist
    return True