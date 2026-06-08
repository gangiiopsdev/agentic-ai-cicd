from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    subprocess.run(['ping', host], check=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_safe(host: str):
    if not validate_host(host):
        raise ValueError("Invalid host")
    subprocess.run(['ping', host], check=True)

def validate_host(host: str) -> bool:
    # Add validation logic here, e.g., allowed IP ranges or domain names
    return True