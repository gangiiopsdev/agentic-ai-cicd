from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation using subprocess.run without shell=True and proper validation
    if not all(c.isalnum() or c in ['.', '-'] for c in host):
        return {"error": "Invalid input"}, 400
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {
        "status": "completed",
        "stdout": result.stdout,
        "stderr": result.stderr
    }