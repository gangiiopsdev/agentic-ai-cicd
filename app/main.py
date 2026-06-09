from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if host.isnumeric() and len(host) <= 3:
        # Safe ping implementation using list arguments and shell=False
        subprocess.call(['ping', '-c', '1', host], shell=False)
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    # Validate input before passing to subprocess
    if not host.isnumeric() or len(host) > 3:
        return {"error": "Invalid host"}, 400
    safe_ping(host)
    return {"status": "completed"}