from fastapi import FastAPI
import subprocess
import re
import shlex

app = FastAPI()

def is_valid_host(host):
    return re.match(r'^[a-zA-Z0-9.-]{1,255}$', host) is not None

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {"status": "failed", "error": "Invalid host name"}
    result = subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True)
    return {
        "status": "completed",
        "output": result.stdout if result.returncode == 0 else result.stderr
    }