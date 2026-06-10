from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    @staticmethod
def ping(host: str):
        # Safe implementation
        args = shlex.split(f"ping {host}")
        subprocess.call(args)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_host(host: str):
    # Validate input to prevent command injection
    if not host.strip() or '&&' in host or ';' in host:
        return {"status": "error", "message": "Invalid input"}
    SafePing.ping(host)
    return {"status": "completed"}