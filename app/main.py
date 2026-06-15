from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    allowed_hosts = ['127.0.0.1', '::1']  # Restrict allowed hosts
    if host not in allowed_hosts:
        return {"status": "failed", "message": "Invalid host"}
    subprocess.run(["ping", host], check=True)
    return {"status": "completed"}