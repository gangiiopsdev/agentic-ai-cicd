from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    if not validate_host(host):
        return False
    subprocess.call(['ping', host], shell=False)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_secure(host: str):
    if ping(host):
        return {"status": "completed"}
    else:
        return {"status": "failed", "error": "Invalid host"}

def validate_host(host: str) -> bool:
    # Simple validation example, replace with more robust validation logic
    return all(c.isalnum() or c in ['.', '-'] for c in host)