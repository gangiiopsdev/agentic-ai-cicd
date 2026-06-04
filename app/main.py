from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, command: str):
        self.command = command.split()

    def execute(self):
        return subprocess.run(self.command, check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    ping_command = PingCommand(f"ping {host}")
    result = ping_command.execute()
    return {"status": "completed", "result": result.returncode}