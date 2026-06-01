from fastapi import FastAPI
import subprocess
from sanic.response import json

app = FastAPI()

@app.get("/")
def home():
    return json({"message": "Agentic Self-Healing Pipeline"})

@app.get("/ping")
def ping(host: str):
    try:
        # Validate and sanitize input to prevent command injection
        if not host.isalnum() or len(host) > 255:
            return json({"status": "failed", "error": "Invalid host name"}, status_code=400)
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return json({"status": "completed", "output": output.stdout})
    except subprocess.CalledProcessError as e:
        return json({"status": "failed", "error": str(e)}, status_code=500)