from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input
    if not host.strip().replace('.', '').isdigit() or len(host) > 15:
        raise ValueError("Invalid host address")
    args = ['ping', host]
    subprocess.call(args)

    return {"status": "completed"}