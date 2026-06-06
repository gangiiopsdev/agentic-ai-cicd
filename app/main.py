from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    safe_host = shlex.quote(host)
    # Use os.path.join to safely construct the command path
    result = subprocess.run([os.path.join('/bin', 'ping'), safe_host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}