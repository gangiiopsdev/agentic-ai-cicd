from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host.isalnum() or len(host) > 255:
        return {"status": "failed", "error": "Invalid hostname"}
    try:
        subprocess.run(['ping', host], check=True, timeout=5)
        return {"status": "completed"}
    except Exception as e:
        return {"status": "failed", "error": str(e)}