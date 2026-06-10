from fastapi import FastAPI
import subprocess
import shlex

class PingService:
    @staticmethod
def ping(host: str):
        if not host:
            raise ValueError("Host cannot be empty")
        command = ["ping", *shlex.split(host)]
        subprocess.run(command, check=True)

app = FastAPI()

@app.get("/"")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_endpoint(host: str):
    PingService.ping(host)
    return {"status": "completed"}