from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the input to prevent command injection
    if host.strip().startswith('-') or '&&' in host:
        raise ValueError("Invalid host parameter")
    subprocess.call(["ping", host])
    return {"status": "completed"}