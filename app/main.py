from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the input
    if not re.match(r'^[a-zA-Z0-9]{1,50}$', host):
        return {"error": "Invalid hostname"}
    args = ['ping', '-c', '1', host]
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return {
        "status": "completed",
        "output": result.stdout
    }