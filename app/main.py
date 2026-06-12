from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        return subprocess.run(['ping', self.host], capture_output=True, text=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the input to ensure it's a safe hostname or IP address
    if not host.isalnum() and '-' not in host:
        raise ValueError('Invalid host name')
    ping_command = PingCommand(host)
    result = ping_command.execute()
    return {
        "status": "completed",
        "output": result.stdout,
        "error": result.stderr if result.returncode != 0 else None
    }