from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if host in ['example.com', '127.0.0.1']:  # Add a whitelist of allowed hosts
        subprocess.run(["ping", host], check=True)
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}