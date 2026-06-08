from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/"),
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input
    if not host.strip() or len(host) > 255:
        return {"status": "error", "message": "Invalid hostname"}

    # Secure implementation with complete path
    subprocess.call(["/bin/ping", host])
    return {"status": "completed"}