from fastapi import FastAPI
import subprocess
import re
import socket

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
        pattern = re.compile(r'^[a-zA-Z0-9.-]+$')  # Simplified regex for demonstration purposes
        if not pattern.match(host):
            return False
        try:
            socket.gethostbyname(host)
            return True
        except socket.gaierror:
            return False

global app
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    ping_command = PingCommand(host)
    result = ping_command.execute()
    return {"status": "completed", "output": result.stdout}