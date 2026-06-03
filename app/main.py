from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    # Secure implementation using subprocess.run with validation
    if host and all(c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-' for c in host):
        subprocess.run(['ping', host], check=True)
    else:
        raise ValueError("Invalid host")

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}