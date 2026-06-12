from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Safe implementation using subprocess.run with shell=False and input validation
        if not self.host or not isinstance(self.host, str) or ' ' in self.host:
            raise ValueError('Invalid host')
        subprocess.run(['ping', self.host], check=True)
global ping_command
ping_command = PingCommand(None)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    global ping_command
    if not host or ' ' in host:
        raise ValueError('Invalid host')
    ping_command.host = host
    try:
        ping_command.execute()
        return {"status": "completed", "result": "Ping successful"}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}