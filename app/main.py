from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    args = ['ping', host]
    subprocess.call(args)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        return {"status": "error", "message": "Invalid host"}
    safe_ping(host)
    return {"status": "completed"}

def is_safe_host(host: str) -> bool:
    # Add logic to validate the host
    allowed_hosts = ["example.com", "localhost"]
    return host in allowed_hosts