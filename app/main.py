from fastapi import FastAPI
import subprocess
import shlex

class SafePing:
    @staticmethod
def safe_execute(command: str, host: str):
        cmd_parts = shlex.split(command)
        cmd_parts.append(host)
        subprocess.run(cmd_parts, check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    SafePing.safe_execute("ping", host)
    return {"status": "completed"}