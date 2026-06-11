from fastapi import FastAPI
import subprocess
import shlex
class CommandExecutor:
    @staticmethod
def execute(command):
        args = shlex.split(command)
        return subprocess.run(args, capture_output=True, text=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = f'ping -c 1 {host}'
    result = CommandExecutor.execute(command)
    return {"status": "completed", "output": result.stdout}