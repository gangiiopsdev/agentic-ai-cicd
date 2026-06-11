from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host parameter
    if not host.isalnum() or len(host) > 255:
        return {"error": "Invalid input"}, 400
    args = ['ping', host]
    subprocess.call(args)
    return {"status": "completed"}