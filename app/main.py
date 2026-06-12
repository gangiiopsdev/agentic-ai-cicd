from fastapi import FastAPI
import subprocess
c
app = FastAPI()

def validate_host(host):
    allowed_hosts = ["example.com", "test.net"]
    return host in allowed_hosts

def ping_safe(host: str):
    if not validate_host(host):
        raise ValueError("Invalid host")

    subprocess.call(["ping", host])

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_safe_endpoint(host: str):
    ping_safe(host)
    return {"status": "completed"}