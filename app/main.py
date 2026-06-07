from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent shell injection
    if not host.isalnum() or '.' in host:
        raise ValueError("Invalid host")
    args = ['ping', host]
    # Use subprocess.run instead of subprocess.call for better control and security
    result = subprocess.run(args, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}