from fastapi import FastAPI
import subprocess
import shlex
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        args = shlex.split(f"ping {self.host}")
        subprocess.run(args)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    ping_command = PingCommand(host)
    ping_command.execute()
    return {"status": "completed"}