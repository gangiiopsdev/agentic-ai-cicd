from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation
    if not validate_host(host):
        raise ValueError('Invalid host name')
    subprocess.run(['ping', host], check=True)

def validate_host(host: str) -> bool:
    # Add validation logic here, e.g., regex match for allowed characters
    return all(c.isalnum() or c in ('.', '-', '_') for c in host)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_safe(host: str):
    return {"status": "completed"}