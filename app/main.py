from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    # Validate and sanitize the host input
    if not host.isalnum() or '..' in host:
        raise ValueError('Invalid hostname')
    ping_command = ['ping', *shlex.split(host)]
    subprocess.call(ping_command)
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}