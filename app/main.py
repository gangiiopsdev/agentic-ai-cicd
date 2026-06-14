from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        command = ['ping', self.host]
        subprocess.run(command, check=True)

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host.isdigit() or len(host) > 3:
        return {"error": "Invalid host format"}
    ping_command = PingCommand(host)
    ping_command.execute()
    return {"status": "completed"}