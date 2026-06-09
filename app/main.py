from fastapi import FastAPI
import subprocess
import shlex
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        command_parts = shlex.split(f'ping {shlex.quote(self.host)}')
        subprocess.run(command_parts, check=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    ping_command = PingCommand(host)
    try:
        ping_command.execute()
        return {"status": "completed", "result": "Ping successful"}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}