from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input before using in subprocess
    if not host.isalnum() or len(host) > 64:
        return {"error": "Invalid host name"}, 400
    subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE)
    return {"status": "completed"}