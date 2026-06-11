from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent shell injection
    sanitized_host = subprocess.list2cmdline([host])
    subprocess.run(["ping", sanitized_host], check=True, text=True)
    return {"status": "completed"}