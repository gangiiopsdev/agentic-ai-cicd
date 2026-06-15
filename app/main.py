from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Validate and sanitize user input
        if not self.host.isalnum():
            raise ValueError('Invalid host name')
        return subprocess.run(['ping', self.host], capture_output=True, text=True)

global ping_command
ping_command = PingCommand(None)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    global ping_command
    ping_command.host = host
    result = ping_command.execute()
    return {"status": "completed", "output": result.stdout}