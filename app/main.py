from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Use subprocess.run instead of subprocess.call and avoid shell=True
        result = subprocess.run(['ping', self.host], capture_output=True, text=True)
        return result.stdout

global app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    ping_command = PingCommand(host)
    status = ping_command.execute()
    return {"status": "completed", "result": status}