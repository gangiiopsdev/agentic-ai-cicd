from fastapi import FastAPI
import subprocess

class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Safe implementation with input validation
        if self.is_valid_host(self.host):
            subprocess.call(['ping', self.host], shell=False)
        else:
            raise ValueError('Invalid host provided')

    @staticmethod
    def is_valid_host(host):
        # Basic validation logic, replace with more robust checks as needed
        return host.replace('.', '').isalnum()

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    ping_command = PingCommand(host)
    ping_command.execute()
    return {"status": "completed"}