from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    # Safe implementation using subprocess.run with shlex.quote
    command = ['ping', shlex.quote(host)]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout
app = FastAPI()
@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input before using it in the command
    if not host.isalnum():
        raise ValueError("Invalid input")
    return {"status": safe_ping(host)}