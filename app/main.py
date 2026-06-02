from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Ensure host is sanitized or validated
    subprocess.run(['ping', host], check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_safe(host: str):
    # Add validation or sanitization of host input
    if not host.isdigit():  # Example validation, replace with actual logic
        raise ValueError("Invalid host")
    return ping(host)