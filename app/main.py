from fastapi import FastAPI
import subprocess
import re

class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Validate the host input to ensure it is a valid hostname or IP address
        if not self.is_valid_host(self.host):
            raise ValueError('Invalid host provided')
        command = ["ping", self.host]
        return subprocess.run(command, capture_output=True, text=True)

    def is_valid_host(self, host):
        # Regular expression to validate IP addresses and hostnames
        pattern = re.compile(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$|^(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$')
        return bool(pattern.match(host))

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    ping_command = PingCommand(host)
    result = ping_command.execute()
    return {"status": "completed", "output": result.stdout}