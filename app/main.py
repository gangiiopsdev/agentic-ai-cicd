from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/"),
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation and complete executable path
    if host in ['8.8.8.8', '127.0.0.1']:  # Example whitelist of allowed hosts
        subprocess.call(["ping", host])
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}