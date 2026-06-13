from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation using subprocess.run with validation and sanitization
    allowed_hosts = ['google.com', 'example.com']  # Add more allowed hosts as needed
    if host in allowed_hosts:
        result = subprocess.run(["ping", host], capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    else:
        return {"error": "Invalid host"}