from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Safer implementation using subprocess.run with shell=False and list of arguments
        result = subprocess.run(['ping', self.host], capture_output=True, text=True)
        return result.stdout

global_ping_command = PingCommand(None)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    global_ping_command.host = host
    return {"status": global_ping_command.execute()}