from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation with input validation
    if all(c.isalnum() or c in '-.' for c in host) and len(host) <= 255:
        subprocess.run(['ping', host], check=True)
    return {"status": "completed"}