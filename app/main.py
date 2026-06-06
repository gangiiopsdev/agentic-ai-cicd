from fastapi import FastAPI
import subprocess

def safe_ping(host):
    # Validate input to prevent excessive or malicious requests
    if not host.strip() or len(host) > 255:
        raise ValueError('Invalid host')
    args = ['ping', '-c', '4', host]  # Limit the number of pings for security and performance reasons
    return subprocess.run(args, capture_output=True, text=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {"status": "completed", "output": result.stdout}