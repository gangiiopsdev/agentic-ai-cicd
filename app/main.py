from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Safe implementation using subprocess.run with shell=False and validate host input
        if not self.host.isalnum():
            raise ValueError('Invalid host input')
        args = ['ping', self.host]
        result = subprocess.run(args, capture_output=True, text=True)
        return {'output': result.stdout}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    result = command.execute()
    return result