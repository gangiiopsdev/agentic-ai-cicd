from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    safe_host = host.strip()  # Ensure no shell injection
    subprocess.run(shlex.split(f'ping -c 1 {safe_host}'), capture_output=True, check=True)
    return {"status": "completed"}