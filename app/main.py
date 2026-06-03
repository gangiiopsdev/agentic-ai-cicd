from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    cmd = ['ping', host]
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return result.stdout
def validate_host(host: str) -> bool:
    if host.strip().startswith('-') or not host.isalnum():  # Prevent potential for shell options and invalid characters
        return False
    return True

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"status": "failed", "message": "Invalid host parameter"}
    output = safe_ping(host)
    return {"status": "completed", "output": output}