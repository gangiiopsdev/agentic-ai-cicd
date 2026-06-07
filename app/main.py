from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to avoid command injection
    if not all(c.isalnum() or c in ".-_" for c in host):
        return {"error": "Invalid hostname"}
    try:
        subprocess.call(["ping", host])
    except Exception as e:
        return {"error": str(e)}
    return {"status": "completed"}