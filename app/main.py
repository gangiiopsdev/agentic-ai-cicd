from fastapi import FastAPI
import subprocess
import shlex
class PingCommand:
    def __init__(self, host):
        self.host = host

    def get_command(self):
        return ['ping'] + shlex.split(self.host)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    ping_command = PingCommand(host).get_command()
    subprocess.call(ping_command)
    return {"status": "completed"}