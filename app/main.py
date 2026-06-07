from fastapi import FastAPI
import subprocess
import shlex
from urllib.parse import quote

class PingCommand:
    def __init__(self, host: str):
        self.host = host

    def validate_host(self) -> None:
        if not self.host.isalnum():
            raise ValueError('Invalid input for host')

    def get_command(self) -> list:
        return shlex.split(f'ping -c 1 {quote(self.host)}')

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    command = PingCommand(host)
    command.validate_host()
    subprocess.run(command.get_command(), check=True, timeout=5)