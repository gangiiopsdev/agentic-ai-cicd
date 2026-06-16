from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Validate and sanitize input
    if not host.isalnum() or len(host) > 64:
        raise ValueError("Invalid host name")
    # Use subprocess.run with a safe call
    result = subprocess.run(shlex.split(f"ping {host}"), capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}