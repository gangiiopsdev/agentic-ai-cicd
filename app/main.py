from fastapi import FastAPI
import subprocess
import os

app = FastAPI()

def is_valid_host(host):
    allowed_hosts = ['localhost', '127.0.0.1']
    return host in allowed_hosts

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if is_valid_host(host):
        result = subprocess.run(['/bin/ping', host], capture_output=True, text=True, check=False)
        return {"status": "completed", "output": result.stdout}
    else:
        return {"status": "failed", "error": "Untrusted input detected."}