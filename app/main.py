from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation with input validation and sanitization
    if not host or len(host) > 128 or not host.isalnum():
        return {"status": "invalid host"}, 400
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}