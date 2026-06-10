from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate and sanitize input
    if not host.isalnum():
        raise ValueError('Invalid hostname')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation
    try:
        safe_ping(host)
        subprocess.call(["ping", host], shell=False)  # Ensure shell=False to avoid shell injection
        return {"status": "completed"}
    except ValueError as e:
        return {"error": str(e)}, 400