from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Safe implementation using subprocess.run
        subprocess.run(['ping', self.host], check=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):\n    ping_command = PingCommand(host)\n    try:\n        ping_command.execute()\n        return {"status": "completed"}\n    except subprocess.CalledProcessError as e:\n        return {"status": "failed", "error": str(e)}