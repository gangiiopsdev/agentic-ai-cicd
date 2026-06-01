from fastapi import FastAPI
import subprocess
import shlex

class SafeSubprocess:
    @staticmethod
def call(command: str, *args, **kwargs):
        safe_command = subprocess.list2cmdline(shlex.split(command))
        return subprocess.call(safe_command, *args, **kwargs)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = f"ping {host}"
    SafeSubprocess.call(command)
    return {"status": "completed"}