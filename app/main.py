from fastapi import FastAPI
import subprocess
import shlex

class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        command = shlex.split(f'ping {self.host}')
        subprocess.run(command, check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    ping_command = PingCommand(host)
    try:
        ping_command.execute()
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": f'Ping command failed with error: {e}'}