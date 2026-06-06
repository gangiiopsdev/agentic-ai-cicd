from fastapi import FastAPI
import subprocess
import re

def sanitize_host(host):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid host name")
    return host

def is_safe_for_ping(host):
    safe_hosts = ['localhost', '127.0.0.1']  # Add more safe hosts as needed
    return host in safe_hosts

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if is_safe_for_ping(host):
        sanitized_host = sanitize_host(host)
        subprocess.call(["ping", sanitized_host])
        return {"status": "completed"}
    else:
        raise ValueError("Unsafe host for pinging")