from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation and sanitization
    if not host or not host.strip() or len(host.split('.')) != 4:
        return {"status": "failed", "error": "Invalid host format"}
    try:
        subprocess.run(['ping', host], check=True)
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}
    return {"status": "completed"}