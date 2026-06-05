from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Validate input to ensure it's safe to use in the command
        if not self.host.isnumeric():
            raise ValueError('Invalid host input')
        subprocess.call(['ping', self.host], shell=False)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    try:
        command.execute()
        return {"status": "completed"}
    except ValueError as e:
        return {"error": str(e)}