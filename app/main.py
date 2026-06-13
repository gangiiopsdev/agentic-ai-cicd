from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation with validation
    safe_host = host.strip()
    if not safe_host.isalnum() or len(safe_host) > 50:
        return {"error": "Invalid host name"}, 400
    subprocess.run(["ping", safe_host], check=True)
    return {"status": "completed"}