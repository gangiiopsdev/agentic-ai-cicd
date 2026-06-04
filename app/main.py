from fastapi import FastAPI
import subprocess
import shlex
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        return subprocess.run(['ping', *shlex.split(self.host)], capture_output=True, text=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    ping_command = PingCommand(shlex.quote(host))
    result = ping_command.execute()
    return {
        "status": "completed",
        "output": result.stdout,
        "stderr": result.stderr
    }