from fastapi import FastAPI
import subprocess
app = FastAPI()

c
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

c
@app.get("/ping")
def ping(host: str):
    # Input validation and sanitization
    if not host.isalnum() or len(host) > 64:
        return {"status": "failed", "error": "Invalid host name"}
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}