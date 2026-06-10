from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Using subprocess.run instead of subprocess.call and avoiding shell=True for security
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        raise Exception("Invalid host")
    output = safe_ping(host)
    return {"status": "completed", "output": output}

import re
def is_safe_host(host: str) -> bool:
    # Regular expression to allow only valid IP addresses and domain names
    pattern = r'^([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}|[a-zA-Z0-9.-]+)$'
    return re.match(pattern, host) is not None