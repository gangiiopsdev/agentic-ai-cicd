from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Validate and sanitize input
        if not self.is_valid_host(self.host):
            raise ValueError("Invalid host")
        return subprocess.run(['ping', self.host], capture_output=True, text=True)

    @staticmethod
    def is_valid_host(host):
        # Basic validation: ensure host contains only alphanumeric characters and hyphens
        return all(c.isalnum() or c == '-' for c in host)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    ping_command = PingCommand(host)
    status, output = ping_command.execute()
    return {"status": status, "output": output}