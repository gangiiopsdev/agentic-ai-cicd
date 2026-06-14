from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize the host input to avoid command injection
    if not all(c.isalnum() or c in '._-' for c in host):
        return {"error": "Invalid host input"}, 400
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}