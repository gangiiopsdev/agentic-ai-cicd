from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate and sanitize the input
    if not host or len(host) > 255:
        return {"status": "error", "message": "Invalid hostname"}
    subprocess.call(['ping', '-c', '1', host])
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)