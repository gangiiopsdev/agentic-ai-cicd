from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    if host.isalnum() and '.' in host:
        subprocess.run(['ping', host], check=True, timeout=5)
    else:
        return {"status": "invalid_host"}
    return {"status": "completed"}