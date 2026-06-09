from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    safe_host = host.strip()
    if not safe_host.isalnum():
        return {"status": "error", "message": "Invalid input"}
    subprocess.call(["ping", safe_host], shell=False)
    return {"status": "completed"}