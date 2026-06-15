from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation and full executable path
    if host not in ['127.0.0.1', '::1']:  # Restrict allowed hosts
        return {"status": "failed", "message": "Invalid host"}
    subprocess.run(["/bin/ping", host], check=True)
    return {"status": "completed"}