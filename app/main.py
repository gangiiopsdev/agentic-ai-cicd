from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    def execute(self):
        return subprocess.call(['ping', self.host], shell=False)

global_ping_command = PingCommand('')

app = FastAPI()

@app.get("/ping")
def ping_host(host: str):
    global_ping_command.host = host
    return global_ping_command.execute()