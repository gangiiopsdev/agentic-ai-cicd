from fastapi import FastAPI
import subprocess
import re
import shlex
def validate_host(host: str) -> bool:
    return re.match(r'^[a-zA-Z0-9.-]+$', host)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"status": "failed", "error": "Invalid hostname"}

    try:
        result = subprocess.run(shlex.split(f'ping -c 1 {host}'), check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}