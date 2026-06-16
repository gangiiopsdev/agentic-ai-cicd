from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        return subprocess.call(['ping', self.host], capture_output=True, text=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    # Sanitize input to prevent command injection
    if not host.isalnum() or len(host) > 255:
        return {"status": "error", "message": "Invalid host name"}
    result = command.execute()
    return {"status": "completed", "output": result}