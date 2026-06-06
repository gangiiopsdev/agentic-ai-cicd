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
        try:
            result = subprocess.run(['/bin/ping', host], capture_output=True, text=True, check=True)
            return {"status": "completed", "output": result.stdout}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": str(e)}
    else:
        return {"status": "failed", "error": "Untrusted input detected."}