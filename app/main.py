from fastapi import FastAPI
import subprocess
import shlex
import os

class PingCommand:
    def __init__(self, host: str):
        self.host = host

    def validate_host(self) -> bool:
        try:
            int(self.host)
            return True
        except ValueError:
            return False

    def execute_command(self) -> dict:
        if not self.validate_host():
            return {'status': 'error', 'message': 'Invalid input'}
        command = shlex.split(f'ping -c 1 {shlex.quote(self.host)}')
        try:
            result = subprocess.run(command, check=True, capture_output=True, text=True)
        except subprocess.CalledProcessError as e:
            return {'status': 'error', 'message': str(e.stderr) if e.stderr else str(e.stdout)}
        return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    command = PingCommand(host)
    return command.execute_command()