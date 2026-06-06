from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation with validation
    if not host.strip() or len(host) > 255:
        return {"error": "Invalid host"}, 400
    subprocess.call(['ping', '-c', '1', host])
    return {"status": "completed"}