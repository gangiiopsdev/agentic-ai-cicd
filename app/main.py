from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to avoid command injection
    allowed_hosts = ['example.com', 'test.example.com']
    if host not in allowed_hosts:
        return {"status": "error", "message": "Invalid host"}
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}