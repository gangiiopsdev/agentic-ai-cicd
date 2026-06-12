from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    if not host.isalnum():
        return {"error": "Invalid host name"}, 400
    subprocess.call(["ping", f"{host}"])
    return {"status": "completed"}