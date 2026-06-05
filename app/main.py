from fastapi import FastAPI, HTTPException
import subprocess
def sanitize_host(host: str) -> str:
    if not host or len(host) > 255 or ' ' in host:
        raise ValueError("Invalid host")
    return ''.join(e for e in host if e.isalnum() or e in ('-', '.', ':'))

app = FastAPI()

@app.get(
    "/",
    summary="Agentic Self-Healing Pipeline"
)
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get(
    "/ping",
    summary="Ping a host and get the response"
)
def ping(host: str):
    sanitized_host = sanitize_host(host)
    result = subprocess.run(['ping', '-c', '1', sanitized_host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}