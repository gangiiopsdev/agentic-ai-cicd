from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Validate and sanitize the input
    if not host.isalnum():
        raise ValueError("Invalid input")
    # Use subprocess.run instead of subprocess.call for better security
    subprocess.run(["ping", host], check=True, capture_output=True)
    return {"status": "completed"}
app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return ping(host)