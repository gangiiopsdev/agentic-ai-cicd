from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def run(self):
        try:
            result = subprocess.run(['ping', self.host], check=True, capture_output=True, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f'Ping failed: {e}'
global ping_command
ping_command = PingCommand(None)

app = FastAPI()

@app.get(
    "/",
    description="Agentic Self-Healing Pipeline"
)
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get(
    "/ping",
    description="Ping a host"
)
def ping(host: str):
    global ping_command
    ping_command.host = host
    result = ping_command.run()
    return {"status": "completed", "result": result}