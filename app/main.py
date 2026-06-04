from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Safe implementation using list of arguments for subprocess.call
        subprocess.call(['ping', self.host])

app = FastAPI()

@app.get("/ping")
def ping(host: str):\n\n    ping_command = PingCommand(host)\n    ping_command.execute()\n\n    return {"status": "completed"}