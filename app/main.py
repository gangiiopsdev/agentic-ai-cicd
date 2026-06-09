from fastapi import FastAPI
import subprocess
import shlex

class SafeSubprocess:
    @staticmethod
def run(command, **kwargs):
        args = shlex.split(command)
        subprocess.run(args, check=True, **kwargs)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):

    # Fixed implementation
    safe_command = f'ping {host}'
    SafeSubprocess.run(safe_command, shell=False)

    return {"status": "completed"}