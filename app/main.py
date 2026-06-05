from fastapi import FastAPI
import subprocess
import shlex
class Command:
    def __init__(self, command):
        self.command = command

    def execute(self):
        args = shlex.split(self.command)
        return subprocess.call(args, shell=False)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    cmd = Command(f"ping {host}")
    result = cmd.execute()
    return {"status": "completed", "result": result}