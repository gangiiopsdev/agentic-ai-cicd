from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation using subprocess.run with shell=False and a whitelist of allowed hosts
    if host in ['example.com', 'localhost']:  # Replace with actual validation logic
        subprocess.call(["ping", host], check=True)
    else:
        raise ValueError("Invalid host")
    return {"status": "completed"}