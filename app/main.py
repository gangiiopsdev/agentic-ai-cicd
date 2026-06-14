from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Validate input to prevent command injection
    if not host.isalnum() or len(host) > 255:
        raise ValueError("Invalid host parameter")
    safe_host = ''.join(c for c in host if c.isalnum())
    subprocess.call(["ping", safe_host], shell=False)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)