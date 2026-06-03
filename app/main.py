from fastapi import FastAPI
import subprocess
import shlex
global ping_lock = False

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    global ping_lock
    if ping_lock:
        return {"status": "already running"}
    ping_lock = True
    try:
        # Validate input to prevent command injection
        if not host.replace('.', '').isdigit():
            raise ValueError("Invalid hostname")
        args = shlex.split(f"ping -c 4 {host}")
        subprocess.run(args, check=True)
        return {"status": "completed"}
    finally:
        ping_lock = False