from fastapi import FastAPI
import subprocess
import re

class PingService:
    @staticmethod
def ping(host: str):
        # Validate and sanitize the host input
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            raise ValueError("Invalid host")
        args = ['ping', '-c', '1', host]
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return result.stdout

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    try:
        return PingService.ping(host)
    except subprocess.CalledProcessError as e:
        return {"error": "Ping failed", "stdout": e.stdout, "stderr": e.stderr}

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}