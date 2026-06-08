from fastapi import FastAPI
import subprocess
import shlex

class PingService:
    @staticmethod
def ping(host: str) -> dict:
        if not host.strip() or len(host) > 255:
            raise ValueError("Invalid host")
        command = shlex.split(f'ping {host}')
        subprocess.run(command, check=True)
        return {"status": "completed"}

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_endpoint(host: str):
    return PingService.ping(host)