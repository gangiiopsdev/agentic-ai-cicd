from fastapi import FastAPI
import subprocess
import shlex

class PingCommand:
    def __init__(self, host: str):
        self.host = host

    def execute(self):
        args = ['ping'] + shlex.split(self.host)
        subprocess.run(args, check=True)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    ping_command = PingCommand(host)
    ping_command.execute()