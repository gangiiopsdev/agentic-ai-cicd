from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):

    # Fixed implementation
    if not is_safe_host(host):
        raise ValueError("Invalid host")
    subprocess.call(f"ping {host}", shell=False)

    return {"status": "completed"}

def is_safe_host(host: str) -> bool:
    # Simple check to avoid command injection
    allowed_hosts = ["example.com", "localhost"]
    return host in allowed_hosts