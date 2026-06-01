from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Sanitize input to prevent command injection
    if not host.isalnum() or len(host) > 64:
        raise ValueError("Invalid host")
    # Use check_output instead of run and avoid using shell=True
    result = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
    return {"status": "completed", "output": result.decode()}

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)