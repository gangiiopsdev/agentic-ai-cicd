from fastapi import FastAPI
import subprocess
import os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host or len(host) > 255:
        return {"status": "failed", "error": "Invalid input"}
    # Secure implementation using subprocess.run
    try:
        result = subprocess.run(['ping', os.path.abspath(host)], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}