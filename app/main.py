from fastapi import FastAPI
import subprocess
import shlex
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Safe implementation with shlex to handle shell injection risks
        args = ['ping'] + shlex.split(self.host)
        subprocess.call(args)

app = FastAPI()

@app.get("/ping")
def ping(host: str):\n    ping_command = PingCommand(host)\n    ping_command.execute()\n    return {"status": "completed"}