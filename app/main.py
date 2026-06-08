from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate and sanitize host input
    if not host.isdigit() or len(host) > 15:
        raise ValueError("Invalid host format")
    args = ['ping', '-c', '1', host]
    subprocess.run(args, check=True)

app = FastAPI()

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}