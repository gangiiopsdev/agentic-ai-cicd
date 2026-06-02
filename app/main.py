from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Whitelist of allowed hosts
    allowed_hosts = ['127.0.0.1', '::1']  # Example allowed IPs
    if host not in allowed_hosts:
        return {"status": "failed", "error": "Invalid host input"}
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}