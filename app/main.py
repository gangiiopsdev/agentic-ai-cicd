from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def run(self):
        # Safe implementation using subprocess.run with shell=False
        result = subprocess.run(['ping', self.host], capture_output=True, text=True)
        return result.stdout
global ping_command
ping_command = PingCommand(None)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    ping_command.host = host
    result = ping_command.run()
    return {"status": "completed", "output": result}