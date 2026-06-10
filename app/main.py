from fastapi import FastAPI
import subprocess
def secure_ping(host: str):
    # Sanitize input to prevent shell injection
    sanitized_host = subprocess.list2cmdline([host])
    subprocess.call(['ping', sanitized_host])

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    secure_ping(host)
    return {"status": "completed"}