from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/""
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input to prevent injection attacks
    if not host.isalnum():
        raise ValueError("Invalid host name")
    try:
        subprocess.run(['ping', host], check=True)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}