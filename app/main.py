from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    async def execute(self):
        # Safe implementation using subprocess.run with shell=False and explicit args
        subprocess.run(['ping', self.host], check=True)

global ping_command
ping_command = PingCommand(host="")

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    global ping_command
    ping_command.host = host
    await ping_command.execute()
    return {"status": "completed"}