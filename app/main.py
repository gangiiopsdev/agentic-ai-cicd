from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        args = ['ping', self.host]
        subprocess.run(args, check=True, capture_output=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):\n    if not host.isalnum():  # Basic validation to prevent injection\n        return {"error": "Invalid input"}\n    command = PingCommand(host)\n    command.execute()\n    return {"status": "completed"}