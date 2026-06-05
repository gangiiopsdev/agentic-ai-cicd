from fastapi import FastAPI
import subprocess
import shlex
import re

class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Validate input to prevent command injection
        if not re.match(r'^[a-zA-Z0-9.-]+$', self.host):
            raise ValueError('Invalid hostname or IP address')
        args = shlex.split(f'ping {self.host}')
        subprocess.call(args)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    try:
        command.execute()
        return {"status": "completed"}
    except ValueError as e:
        return {"error": str(e)}