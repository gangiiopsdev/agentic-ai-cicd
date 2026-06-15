from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Enhanced input validation and use of a safe alternative to subprocess.call
    if not host.isalnum() or len(host) > 255:
        return {"status": "failed", "error": "Invalid host"}
    result = subprocess.run(["ping", host], capture_output=True, text=True, check=False)
    return {"status": "completed", "output": result.stdout}