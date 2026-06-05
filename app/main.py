from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        command = ["ping", self.host]
        subprocess.run(command, check=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):\n    # Secure implementation\n    try:\n        ping_command = PingCommand(host)\n        ping_command.execute()\n        return {"status": "completed"}\n    except subprocess.CalledProcessError as e:\n        return {"error": str(e)}