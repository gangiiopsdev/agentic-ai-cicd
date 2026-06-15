from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Secure implementation using a list for the command arguments
        args = ['ping', self.host]
        subprocess.run(args, check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    ping_command = PingCommand(host)
    ping_command.execute()
    return {"status": "completed"}