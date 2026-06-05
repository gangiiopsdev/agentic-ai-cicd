from fastapi import FastAPI
import subprocess
def sanitize_host(host):
    if not host.isalnum() or len(host) > 100:
        raise ValueError("Invalid host name")
    return host.strip()

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    sanitized_host = sanitize_host(host)
    args = ['ping', sanitized_host]
    subprocess.run(args, check=True)
    return {"status": "completed"}