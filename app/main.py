from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize host input
    if not is_valid_host(host):
        return {"status": "error", "message": "Invalid host name"}
    subprocess.call(["ping", host])
    return {"status": "completed"}

def is_valid_host(host: str) -> bool:
    # Implement validation logic here
    return all(c.isalnum() or c in ('-', '.', ':') for c in host)