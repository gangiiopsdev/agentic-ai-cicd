from fastapi import FastAPI
import subprocess
import shlex
class PingCommand:
    def __init__(self, host):
        self.host = host

    def validate_host(self):
        if not self.host.isdigit():
            raise ValueError("Invalid host")

app = FastAPI()

@app.get="/ping")
def ping(host: str):
    cmd = PingCommand(host)
    cmd.validate_host()
    args = ['ping', *shlex.split(cmd.host)]
    subprocess.call(args)
    return {"status": "completed"}