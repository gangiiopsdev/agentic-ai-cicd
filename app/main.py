from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        result = subprocess.run(['ping', self.host], check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}

global_ping_command = PingCommand(None)

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    global_ping_command.host = host
    return global_ping_command.execute()