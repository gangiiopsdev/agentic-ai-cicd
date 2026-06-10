from fastapi import FastAPI
import subprocess
def safe_ping(host):
    args = ['ping', '8.8.8.8']  # Replace with a fixed IP or use a whitelist
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input before using it in subprocess
    if not host.isalnum() or len(host) > 20:
        raise ValueError('Invalid host name')
    return safe_ping(host)