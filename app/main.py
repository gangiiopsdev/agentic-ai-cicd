from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize the host input
    if not all(c.isalnum() or c in ['.', '-'] for c in host):
        return {"status": "error", "message": "Invalid hostname"}
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}