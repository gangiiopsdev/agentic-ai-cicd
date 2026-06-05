from fastapi import FastAPI
import subprocess
import shlex

class PingCommand:
    def __init__(self, host: str):
        self.host = host

    def execute(self):
        command = ['ping', *shlex.split(self.host)]
        subprocess.call(command)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command_executor = PingCommand(host)
    command_executor.execute()
    return {"status": "completed"}