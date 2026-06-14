from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation
    if not is_valid_host(host):
        raise ValueError("Invalid host name")
    subprocess.run(["ping", host], check=True)
    return {"status": "completed"}

def is_valid_host(hostname: str) -> bool:
    import re
    return re.match(r'^[a-zA-Z0-9.-]+$', hostname)