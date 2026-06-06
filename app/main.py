from fastapi import FastAPI
import subprocess
import shlex
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    def execute(self):
        command_parts = ['ping', *shlex.split(self.host)]
        subprocess.run(command_parts)

global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    cmd = PingCommand(host)
    cmd.execute()
    return {"status": "completed"}