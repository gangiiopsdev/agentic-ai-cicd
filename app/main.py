from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the input to prevent injection attacks
    if not host.isalnum():
        return {"status": "failed", "error": "Invalid host name"}
    
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    if result.returncode == 0:
        return {"status": "completed", "output": result.stdout}
    else:
        return {"status": "failed", "error": result.stderr}