from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Use subprocess.run instead of subprocess.call with shell=True
        result = subprocess.run(['ping', self.host], capture_output=True, text=True)
        return result.stdout

global ping_command
ping_command = PingCommand(host='')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Update the host property of the PingCommand instance before calling execute
    ping_command.host = host
    return ping_command.execute()