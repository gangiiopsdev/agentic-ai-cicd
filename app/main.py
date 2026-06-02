from fastapi import FastAPI
import subprocess
class CommandExecutor:
    def __init__(self, command: str):
        self.command = command

    def execute(self):
        import shlex
        args = shlex.split(self.command)
        return subprocess.call(args)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    executor = CommandExecutor(f"ping {host}")
    result = executor.execute()
    return {"status": "completed", "result": result}