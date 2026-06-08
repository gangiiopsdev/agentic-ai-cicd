from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the input to prevent injection attacks
    if not host.isalnum() or '.' not in host:
        return {"status": "invalid host"}
    subprocess.run(["ping", host], check=True, capture_output=True, text=True)
    return {"status": "completed"}