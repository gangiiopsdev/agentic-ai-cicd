from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if not host.strip().isdigit():
        raise ValueError("Invalid host")
    return subprocess.call(f"ping {host}", shell=False)

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    return {"status": safe_ping(host)}