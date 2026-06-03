from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate user input
    if not host or not host.strip() or ' ' in host:
        return {"status": "error", "message": "Invalid host"}
    subprocess.run(["ping", host], capture_output=True, text=True)
    return {"status": "completed"}