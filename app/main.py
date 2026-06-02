from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Ensure input is validated and sanitized
    if not host.isalnum():
        raise ValueError("Invalid input")
    subprocess.call(['ping', host], shell=False)
    return {"status": "completed"}