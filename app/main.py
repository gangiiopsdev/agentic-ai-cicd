from fastapi import FastAPI
import subprocess
import shlex

class SafePinger:
    def __init__(self, ping_command: str):
        self.ping_command = ping_command

    def execute(self, host: str) -> None:
        command_parts = shlex.split(f"{self.ping_command} {host}")
        subprocess.call(command_parts)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    pinger = SafePinger(ping_command="ping")
    pinger.execute(host)
    return {"status": "completed"}