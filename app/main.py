from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to avoid command injection
    safe_host = subprocess.quote(host)
    subprocess.call(f"ping {safe_host}", shell=True)

    return {"status": "completed"}