from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate host input to prevent command injection
    if not is_safe_host(host):
        raise ValueError("Invalid host name")
    subprocess.run(["ping", host], check=True)
    return {"status": "completed"}

def is_safe_host(host: str) -> bool:
    # Implement validation logic here, e.g., allow only safe host names or IP addresses
    allowed_hosts = ["example.com", "127.0.0.1"]
    return host in allowed_hosts