from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        # Safe implementation using subprocess.run and shlex.split
        import shlex
        cmd = ['ping', self.host]
        subprocess.run(cmd, check=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):\n    command = PingCommand(host)\n    try:\n        result = command.execute()\n        return {"status": "completed", "result": result}\n    except subprocess.CalledProcessError as e:\n        return {"status": "error", "error": str(e)}