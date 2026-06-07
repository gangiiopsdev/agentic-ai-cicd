from fastapi import FastAPI
import subprocess
def shell_safe_string(s):
    return ''.join(ch for ch in s if ch.isalnum() or ch in ['-', '.', '_', ':', '/', '@'])

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_host = shell_safe_string(host)
    subprocess.call(f"ping {safe_host}", shell=False)
    return {"status": "completed"}