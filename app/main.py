from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Input validation
    if not host.isdigit() or len(host) > 15:
        raise ValueError("Invalid host")
    # Secure implementation
    subprocess.run(["ping", host], check=True, text=True)
    return {"status": "completed"}