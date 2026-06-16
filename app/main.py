from fastapi import FastAPI
import subprocess
import shlex

class SafeSubprocess:
    @staticmethod
def run(command: str, **kwargs):
        args = shlex.split(command)
        return subprocess.run(args, **kwargs)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = f'ping {host}'
    result = SafeSubprocess.run(command, shell=False)
    return {"status": "completed", "stdout": result.stdout.decode() if result.stdout else '', "stderr": result.stderr.decode() if result.stderr else ''}