from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using a whitelist of allowed hosts
    allowed_hosts = ["127.0.0.1", "localhost"]
    if host in allowed_hosts:
        subprocess.run(["ping", host], check=True, capture_output=True, text=True)
    else:
        return {"status": "unauthorized"}

    return {"status": "completed"}