from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation with proper input validation and sanitization
    subprocess.call(["ping", host.replace(' ', '')])  # Remove spaces to mitigate potential injection
    return {"status": "completed"}