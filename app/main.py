from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Validate and sanitize the host parameter
    if not is_valid_host(host):
        raise ValueError('Invalid host')
    subprocess.run(['ping', host], check=True)

def is_valid_host(host):
    # Implement validation logic here (e.g., regex, allowed domains)
    return all(c.isalnum() or c in '.- ' for c in host)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}