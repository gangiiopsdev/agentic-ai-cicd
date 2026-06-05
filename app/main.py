from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Safer implementation using subprocess.run with args and shell=False to prevent shell command injection
        subprocess.run(['ping', self.host], check=True, shell=False)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent injection attacks
    if not host or ' ' in host:
        raise ValueError("Invalid host")
    ping_command = PingCommand(host)
    ping_command.execute()
    return {"status": "completed"}