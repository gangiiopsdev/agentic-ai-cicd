from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if host.startswith('-'):  # Example simple validation, not comprehensive
        raise ValueError("Invalid input")
    subprocess.call(["ping", host])
    return {"status": "completed"}