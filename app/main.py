from fastapi import FastAPI
import subprocess
import re
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    @staticmethod
def safe_ping(host: str):
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            raise ValueError('Invalid host name')
        return PingCommand(host)

    def execute(self):
        subprocess.call(['ping', self.host])

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    command = safe_ping(host)
    command.execute()
    return {"status": "completed"}