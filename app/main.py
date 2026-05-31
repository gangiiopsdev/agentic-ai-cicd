from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not host or 'ping' not in host:
        raise ValueError('Invalid host')
    # Use a whitelist of allowed hosts or commands
    allowed_hosts = ['127.0.0.1', '::1']  # Example allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Host not allowed')
    return subprocess.run(['ping', host], capture_output=True, text=True, check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        result = safe_ping(host)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}