from fastapi import FastAPI
import subprocess
import shlex
global app
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        # Sanitize the input to prevent command injection
        if not host.strip().isdigit():
            raise ValueError("Invalid host")
        subprocess.call(shlex.split(f'ping {host}'))
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e)}