from fastapi import FastAPI
import shlex
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        # Safe implementation using shlex to escape command arguments
        args = ['ping', host]
        subprocess.run(args, check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input to prevent command injection
    if not host.isalnum() or len(host) > 255:
        raise ValueError('Invalid host input')
    SafePing.ping(shlex.quote(host))
    return {"status": "completed"}