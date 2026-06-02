from fastapi import FastAPI
import subprocess
def safe_ping(host: str) -> bool:
    allowed_hosts = ['127.0.0.1', '::1']  # Define allowed hosts
    if host in allowed_hosts:
        return True
    return False

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not safe_ping(host):
        return {"status": "failed", "error": "Host not allowed"}
    try:
        # Using subprocess.run for better security
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}