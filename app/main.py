from fastapi import FastAPI
import shlex
import subprocess

class SafePing:
    def __init__(self):
        self.safe_host = None

    def validate_host(self, host: str):
        if not host.isalnum():
            raise ValueError('Invalid host name')

    def escape_host(self, host: str):
        self.safe_host = shlex.quote(host)

    def execute_command(self):
        subprocess.call(['ping', '-c', '1', self.safe_host], shell=False)

app = FastAPI()
safe_ping_instance = SafePing()

@app.get("/ping")
def ping(host: str):
    safe_ping_instance.validate_host(host)
    safe_ping_instance.escape_host(host)
    safe_ping_instance.execute_command()
    return {"status": "completed"}