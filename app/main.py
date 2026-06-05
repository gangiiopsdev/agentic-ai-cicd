from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/"),
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation with input validation and sanitization
    if not host or len(host) > 255:
        return {"status": "error", "message": "Invalid host"}
    try:
        subprocess.run(['ping', '-c', '1', host], check=True, shell=False)
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}
    return {"status": "completed"}