from fastapi import FastAPI
import shlex
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = shlex.quote(host)

    def execute(self):
        return subprocess.run(['ping', self.host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent shell injection
    if not host.strip().isalnum() or ' ' in host:
        raise ValueError("Invalid host")
    ping_command = PingCommand(host)
    result = ping_command.execute()
    return {"status": result.stdout.decode('utf-8')}