from fastapi import FastAPI
import subprocess

def ping(host: str):
    # Secure implementation
    args = ['ping', host]
    subprocess.run(args, check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with validation and sanitization
    if not host.isalnum() or len(host) > 64:
        raise ValueError("Invalid host name")
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {"status": "completed"}