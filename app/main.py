from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/)")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the input
    if not host.strip().isdigit():
        return {"error": "Invalid input"}, 400
    subprocess.call(['ping', host], shell=False)
    return {"status": "completed"}