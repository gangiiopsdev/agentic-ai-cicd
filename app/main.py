from fastapi import FastAPI
import subprocess
import shlex
from typing import List

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    allowed_hosts = ["example.com", "test.com"]  # Replace with actual list of allowed hosts
    if host not in allowed_hosts:
        return {"status": "error", "error": "Host not allowed"}
    try:
        result = subprocess.run(['ping', shlex.quote(host)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "error": str(e)}

# Preventive controls
# 1. Use a whitelist of allowed hosts
# 2. Avoid using shlex.quote if not necessary for escaping
# 3. Consider using a subprocess wrapper library that provides safer alternatives