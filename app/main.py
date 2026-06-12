from fastapi import FastAPI
import subprocess
import shlex

class SafeCommand:
    @staticmethod
def run(command, *args, **kwargs):
        # Use shlex.split for safe argument splitting
        cmd_parts = shlex.split(command)
        return subprocess.run(cmd_parts, check=True, text=True, *args, **kwargs)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation using SafeCommand
    SafeCommand.run(f'ping', host)
    return {"status": "completed"}