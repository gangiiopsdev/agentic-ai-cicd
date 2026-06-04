from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/"),
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run without shell=True and input validation
    if not host.strip():
        return {"error": "Invalid host parameter"}, 400
    subprocess.run(["ping", host], check=True)
    return {"status": "completed"}