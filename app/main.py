from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host: str):
        # Use subprocess.run for safer execution with proper argument passing
        subprocess.run(['ping', host], check=True, capture_output=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input before passing to safe_ping
    if not host.strip().replace('.', '').isdigit() or len(host) > 255:
        return {"error": "Invalid host"}, 400
    safe_ping(host)
    return {"status": "completed"}