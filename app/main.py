from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input
    if not host.isalnum() or len(host) > 255:
        return {"error": "Invalid host name"}, 400
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}