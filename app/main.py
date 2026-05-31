from fastapi import FastAPI
import subprocess
import shlex

class SafePing:
    @staticmethod
def safe_ping(host: str):
        cmd = ['ping', *shlex.split(host)]
        subprocess.call(cmd)

app = FastAPI()

@app.get="/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping")
def ping(host: str):
    SafePing.safe_ping(host)
    return {"status": "completed"}