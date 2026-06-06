from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = "ping"
    args = shlex.split(host)
    result = subprocess.run([command] + args, capture_output=True, text=True, check=True, timeout=10)
    return {"status": "completed", "output": result.stdout}

# Add input validation and sanitization for `host`
def validate_host(host: str):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890.-_')
    if any(char not in allowed_chars for char in host):
        raise ValueError("Invalid characters in host")