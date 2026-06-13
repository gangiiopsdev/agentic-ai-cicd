from fastapi import FastAPI
import subprocess
import shlex
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Use shlex.quote to safely escape the user input
        safe_host = shlex.quote(self.host)
        return subprocess.run(['ping', safe_host], capture_output=True, text=True)

global app
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    result = command.execute()
    return {"status": "completed", "output": result.stdout}