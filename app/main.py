from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the input before using it in the subprocess call
    if not host.isalnum() or len(host) > 255:
        return {"status": "failed", "error": "Invalid host name"}

    try:
        subprocess.run(['ping', host], check=True, timeout=5)
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

    return {"status": "completed"}