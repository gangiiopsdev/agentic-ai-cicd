from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, command: str):
        self.command = command.split()

    def execute(self):
        return subprocess.run(self.command, check=True, shell=False)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to prevent command injection
    if not all(c.isalnum() or c in ['.', '-', '_'] for c in host):
        return {"error": "Invalid host name"}, 400
    ping_command = PingCommand(f'ping {host}')
    result = ping_command.execute()
    return {"status": "completed", "result": result.returncode}