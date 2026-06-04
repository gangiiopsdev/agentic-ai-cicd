from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    def execute(self):
        args = ['ping', self.host]
        return subprocess.run(args, capture_output=True, text=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    ping_command = PingCommand(host)
    result = ping_command.execute()
    return {
        "status": "completed",
        "stdout": result.stdout,
        "stderr": result.stderr
    }