from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host: str):
    # Safe implementation using subprocess.run without shell=True
    subprocess.run(['ping', host], check=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host parameter
    if not validate_host(host):
        return {"status": "Invalid host"}, 400
    run_ping(host)
    return {"status": "completed"}

def validate_host(host: str) -> bool:
    # Add validation logic here (e.g., allow only specific domains)
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts