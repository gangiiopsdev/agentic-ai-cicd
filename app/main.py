from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation with input validation
    if host.strip() and any(c in host for c in ' 	
'):  # Check for spaces, tabs, newlines
        return {"status": "failed", "message": "Invalid input"}
    subprocess.call(["ping", host], shell=False)
    return {"status": "completed"}