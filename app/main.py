from fastapi import FastAPI
import subprocess

class PingCommand:
    @staticmethod
def execute(host: str):
        args = ['ping', host]
        subprocess.run(args, check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host.isalnum() and '-' not in host:
        raise ValueError("Invalid input for ping host")
    PingCommand.execute(host)
    return {"status": "completed"}