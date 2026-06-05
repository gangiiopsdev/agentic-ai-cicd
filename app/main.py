from fastapi import FastAPI
import subprocess
from typing import Union

app = FastAPI()

def is_safe_host(host: str) -> bool:
    # Define a list of allowed hosts or patterns
    allowed_hosts = ['example.com', 'localhost']
    return any(host.endswith(allowed) for allowed in allowed_hosts)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if is_safe_host(host):
        args = ['ping', host]
        subprocess.call(args)
        return {"status": "completed"}
    else:
        return {"error": "Host not allowed"}