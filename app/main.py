from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to avoid shell injection
    if not is_valid_host(host):
        raise ValueError("Invalid host")
    subprocess.run(["ping", host], check=True, capture_output=True)
    return {"status": "completed"}

def is_valid_host(host: str) -> bool:
    # Implement validation logic here, e.g., allow only IP addresses or specific domain names
    allowed_hosts = ["127.0.0.1", "8.8.8.8"]
    return host in allowed_hosts