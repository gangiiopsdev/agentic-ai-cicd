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
    # Validate the host input to ensure it does not contain malicious content
    if not cls.is_safe_host(host):
        raise ValueError('Invalid host')
    global_ping_command.host = host
    return {"status": global_ping_command.execute()}

@PingCommand.classmethod
def is_safe_host(cls, host: str) -> bool:
    # Implement validation logic for the host input here
    import re
    safe_pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(safe_pattern, host) is not None