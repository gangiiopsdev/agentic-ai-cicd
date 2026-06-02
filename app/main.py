from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    if host in ['google.com', 'github.com']:  # Example allowed hosts
        subprocess.run(["ping", host], check=True)
    else:
        return {"error": "Invalid host"}
    return {"status": "completed"}