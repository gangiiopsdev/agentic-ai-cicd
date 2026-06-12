from fastapi import FastAPI
import subprocess
import shlex
import os

class PingCommand:
    def __init__(self, host: str):
        self.host = host

    def execute(self):
        safe_host = shlex.quote(self.host)
        command = ['ping', safe_host]
        try:
            result = subprocess.run(command, check=True, capture_output=True, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f'Error: {e.output}'

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return PingCommand(host).execute()