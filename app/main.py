from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        args = ['ping', self.host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout

class ValidatedPingCommand(PingCommand):
    def __init__(self, host):
        if not isinstance(host, str) or not host.strip():
            raise ValueError('Invalid host provided')
        super().__init__(host)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = ValidatedPingCommand(host)
    status = command.execute()
    return {"status": "completed", "output": status}