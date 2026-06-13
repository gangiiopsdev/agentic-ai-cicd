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
    # Validate and sanitize user input before using it in subprocess
    if not host or len(host) > 100 or not all(c.isalnum() or c in ".-:" for c in host):
        return {"error": "Invalid host name"}
    command = PingCommand(host)
    result = command.execute()
    return {"status": "completed", "output": result.stdout}