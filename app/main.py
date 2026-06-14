from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    def __init__(self):
        pass

    def execute(self, command_parts: list):
        return subprocess.run(command_parts, capture_output=True, text=True, check=True)

app = FastAPI()
safe_ping_instance = SafePing()
def safe_ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid host')
    command_parts = ['ping', '-c', '1'] + shlex.split(host)
    return safe_ping_instance.execute(command_parts)

@app.get("/ping")
def ping(host: str): return safe_ping(host)