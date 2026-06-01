from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    if not host.isalnum():
        return "Invalid host"
    command = ['ping'] + shlex.split(host)
    result = subprocess.run(command, capture_output=True, text=True)
    return result.returncode

def home():
    return {"message": "Agentic Self-Healing Pipeline"}

def ping(host: str):
    result = safe_ping(host)
    if isinstance(result, int) and result == 0:
        return {"status": "completed", "result": "success"}
    else:
        return {"status": "failed", "result": result}