from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def run(command: str, **kwargs):
        args = shlex.split(command)
        return subprocess.run(args, check=True, capture_output=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_command = f'ping {host}'
    result = SafeSubprocess.run(safe_command, check=True, capture_output=True)
    return {"status": "completed", "output": result.stdout.decode()}