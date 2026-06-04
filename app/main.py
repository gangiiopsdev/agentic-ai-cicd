from fastapi import FastAPI
import subprocess
import shlex
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    def execute(self):
        command_parts = ['ping', *shlex.split(self.host)]
        subprocess.call(command_parts)

global app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    command = PingCommand(host)
    command.execute()
    return {"status": "completed"}