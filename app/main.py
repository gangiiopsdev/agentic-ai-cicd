from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    if host in ['example.com', 'localhost']:  # Add validation for trusted hosts
        subprocess.call(['ping', host], shell=False)
    else:
        return {"status": "error", "message": "Untrusted host"}
    return {"status": "completed"}