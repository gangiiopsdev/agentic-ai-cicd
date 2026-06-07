from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run with input validation
    subprocess.run(['ping', host], check=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_secure(host: str):
    # Validate the input to ensure it does not contain malicious content
    if not host.isalnum() or len(host) > 64:
        raise ValueError("Invalid host name")
    return ping(host)