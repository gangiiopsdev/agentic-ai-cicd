from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        try:
            output = subprocess.run(['ping', self.host], capture_output=True, text=True, check=True)
            return output.stdout
        except subprocess.CalledProcessError as e:
            return str(e)
global ping_command
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    global ping_command
    if not ping_command:
        # Validate the host input to prevent command injection
        if not all(c.isalnum() or c in '-.' for c in host):
            return {"error": "Invalid host name"}
        ping_command = PingCommand(host)
    return {"status": "completed", "output": ping_command.execute()}