from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def run(self):
        command = ['ping', self.host]
        return subprocess.run(command, capture_output=True, text=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):\n    ping_command = PingCommand(host)\n    result = ping_command.run()\n    return {"status": "completed", "stdout": result.stdout}