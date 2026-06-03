from fastapi import FastAPI
import subprocess
import shlex
import os

class SafePing:
    def __init__(self, host):
        self.host = host

    def validate_host(self):
        return os.path.basename(self.host) == self.host

    def execute_command(self):
        if not self.validate_host():
            raise ValueError('Invalid host')
        args = ['ping'] + shlex.split(shlex.quote(self.host))
        subprocess.call(args)

app = FastAPI()

@app.get("/ping")
def ping(host: str):    
    safe_ping = SafePing(host)
    safe_ping.execute_command()
    return {"status": "completed"}