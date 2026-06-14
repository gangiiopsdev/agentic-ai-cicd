from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        args = ['ping', self.host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise ValueError("Invalid host")
    command = PingCommand(host)
    result = command.execute()
    return {"status": "completed", "result": result}
def validate_host(host: str) -> bool:
    # Add logic to validate the host input
    return host.isalnum() and len(host) <= 255}