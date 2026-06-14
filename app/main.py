from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and input validation
    if not host.strip() or len(host.split()) > 1:
        raise ValueError("Invalid host input")
    result = subprocess.run(["ping", host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}