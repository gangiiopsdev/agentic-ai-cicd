from fastapi import FastAPI
import subprocess
from shlex import quote as cmd_quote
class PingCommand:
    def __init__(self, host):
        self.host = host

    def run(self):
        result = subprocess.run(['ping', '-c', '1', cmd_quote(self.host)], capture_output=True, text=True)
        return result.stdout

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    output = command.run()
    return {"status": "completed", "output": output}