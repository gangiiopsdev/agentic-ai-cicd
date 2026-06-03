from fastapi import FastAPI
import subprocess
def safe_ping(host: str) -> str:
    # Sanitize input to prevent injection attacks
    allowed_hosts = ["127.0.0.1", "localhost"]
    if host in allowed_hosts:
        command = ["ping", host]
        result = subprocess.run(command, capture_output=True, text=True)
        return result.stdout
    else:
        return "Invalid host"

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)