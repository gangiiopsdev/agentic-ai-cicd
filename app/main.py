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
        raise ValueError("Unsafe host")
    subprocess.call(['ping', host])

def is_safe_host(hostname):
    # Simple example to check for malicious patterns
    return hostname.isalnum() and '.' in hostname