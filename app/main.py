from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Safe implementation using shlex and subprocess.run
        cmd = ['ping', self.host]
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout

global ping_command
ping_command = PingCommand('')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    global ping_command
    ping_command.host = host
    result = ping_command.execute()
    return {"status": "completed", "output": result}