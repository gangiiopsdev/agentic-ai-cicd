from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Preventive control
    if 'ping' not in host or '\' in host:
        return {"status": "invalid input"}

    # Safe implementation
    subprocess.call(f"ping {host}", shell=False)

    return {"status": "completed"}