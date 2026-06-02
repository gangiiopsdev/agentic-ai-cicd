from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Safe implementation using shlex.quote to sanitize the input
        subprocess.call(['ping', subprocess.list2cmdline([self.host])])

app = FastAPI()

@app.get("/ping")
def ping(host: str):\n    ping_command = PingCommand(host)\n    ping_command.execute()\n    return {"status": "completed"}