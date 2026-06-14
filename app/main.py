from fastapi import FastAPI
import subprocess
import shlex
class PingCommand:
    def __init__(self, host):
        self.host = host
        self.command = shlex.split(f'ping {shlex.quote(host)}')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    subprocess.run(PingCommand(host).command, check=True)
    return {"status": "completed"}