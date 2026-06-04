from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        args = ['ping', self.host]
        subprocess.call(subprocess.list2cmdline(args))

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    cmd = PingCommand(host)
    cmd.execute()