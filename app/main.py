from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    allowed_hosts = ['127.0.0.1', 'localhost']
    if host not in allowed_hosts:
        return {"status": "error", "message": "Invalid host"}
    # Secure implementation using subprocess.run
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}