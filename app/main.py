from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the input
    if not host.strip() or len(host) > 255:
        return{"error": "Invalid host parameter"}, 400
    subprocess.call(["ping", host])
    return {"status": "completed"}