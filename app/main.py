from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Secure implementation using subprocess.run with full path and shell=False
        subprocess.run(['/bin/ping', self.host], check=True)

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    ping_command = PingCommand(host)
    ping_command.execute()
    return {"status": "completed"}