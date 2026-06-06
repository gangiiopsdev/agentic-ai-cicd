from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with argument validation and sanitization
    if host.strip() == "." or host.startswith("-"):
        raise ValueError("Invalid hostname")
    subprocess.call(["ping", host])
    return {"status": "completed"}