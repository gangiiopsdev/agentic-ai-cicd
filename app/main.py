from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent command injection
    if not host.isalnum():
        return {"status": "error", "message": "Invalid input"}
    subprocess.run(shlex.split(f'ping -c 1 {host}'), check=True)
    return {"status": "completed"}