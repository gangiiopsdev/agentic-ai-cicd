from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if not validate_host(host):
        raise ValueError("Invalid host")
    args = ['ping', host]
    subprocess.run(args, check=True)

def validate_host(host):
    # Implement validation logic here (e.g., allow only certain IP addresses or domains)
    allowed_hosts = ['127.0.0.1', '::1']  # Example list of allowed hosts
    return host in allowed_hosts

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}