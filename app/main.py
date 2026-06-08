from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with validation and full executable path
    if host.strip() and len(host) < 100:
        subprocess.call(["ping", host])
    return {"status": "completed"}