from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def run(command, *args, **kwargs):
        args = list(shlex.split(command))
        return subprocess.run(args, **kwargs)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = f"ping {host}"
    result = SafeSubprocess.run(command)
    return {"status": result.returncode}