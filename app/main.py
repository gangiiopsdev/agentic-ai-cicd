from fastapi import FastAPI
import subprocess
import shlex

class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        if self.is_valid_host(self.host):
            command = ['ping', shlex.quote(self.host)]
            subprocess.run(command, check=True)
        else:
            raise ValueError('Invalid host provided')

    @staticmethod
    def is_valid_host(host):
        import re
        return re.match(r'^[a-zA-Z0-9.-]+$', host) is not None

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    ping_command = PingCommand(host)
    ping_command.execute()
    return {"status": "completed"}