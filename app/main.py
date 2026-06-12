from fastapi import FastAPI
import subprocess
from shlex import quote
import shlex

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize host input
    if not host.isalnum() or len(host) > 255:
        return {
            "status": "failed",
            "error": "Invalid host input"
        }
    try:
        result = subprocess.run(shlex.split(f'ping {quote(host)}'), check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {
            "status": "failed",
            "error": str(e)
        }