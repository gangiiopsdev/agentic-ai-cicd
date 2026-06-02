from fastapi import FastAPI
import subprocess
generate_ping_command = lambda host: f'ping {host}' if 'localhost' in host else None

class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        command = ['ping', self.host]
        return subprocess.run(command, check=True, capture_output=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if 'localhost' in host:
        ping_command = PingCommand(host)
        result = ping_command.execute()
        return {"status": "completed", "output": result.stdout.decode()}
    else:
        return {"error": "Invalid host"}