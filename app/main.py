from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Safe implementation using list of arguments for subprocess.call
        subprocess.run(['ping', self.host], check=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):\n
    ping_command = PingCommand(host)\n    ping_command.execute()\n
    return {"status": "completed"}