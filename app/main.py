from fastapi import FastAPI
import subprocess
from sanic.response import text

global ping_sanitize_func
ping_sanitize_func = lambda x: ''.join(e for e in x if e.isalnum() or e in ['.', '-', '_'])

app = FastAPI()

@app.get("/")
def home():
    return text("Agentic Self-Healing Pipeline")

@app.get("/ping")
def ping(host: str):
    sanitized_host = ping_sanitize_func(host)
    try:
        subprocess.run(['ping', sanitized_host], capture_output=True, text=True, check=True)
        return text({"status": "completed"})
    except subprocess.CalledProcessError as e:
        return text({"error": str(e), "status": "failed"})