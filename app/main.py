from fastapi import FastAPI
import subprocess
import shlex
import os

class PingCommand:
    def __init__(self, host):
        self.host = shlex.quote(host)
        self.command = ['ping', self.host]

    def execute(self):
        return subprocess.run(self.command, capture_output=True, text=True, check=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    result = command.execute()
    return {"status": "completed", "output": result.stdout}