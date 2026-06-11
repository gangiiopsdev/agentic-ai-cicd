from fastapi import FastAPI
import subprocess
from shlex import quote

class FastApiApp:
    def __init__(self):
        self.app = FastAPI()

    def run_command(self, command: list):
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout

app_instance = FastApiApp()

def ping(host: str):
    # Sanitize input to prevent command injection
    if not host.isalnum():
        raise ValueError("Invalid host name")
    sanitized_host = quote(host)
    command = ["ping", "-c", "1", sanitized_host]
    return app_instance.run_command(command)

app_instance.app.get(
    "/ping",
    summary="Ping a host",
    description="Sanitize input to prevent command injection",
)(ping)