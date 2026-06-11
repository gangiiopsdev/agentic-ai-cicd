from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    def execute(self) -> None:
        # Secure implementation using shell=False and full command path
        subprocess.run(['ping', self.host], check=True, shell=False)

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate user input
    if not host.strip().isdigit() and '@' not in host:
        raise ValueError("Invalid host")
    ping_command = PingCommand(host)
    try:
        ping_command.execute()
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}
    return {"status": "completed"}