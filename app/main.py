from fastapi import FastAPI
import subprocess
import shlex
class CommandValidator:
    def __init__(self, allowed_commands):
        self.allowed_commands = set(allowed_commands)

    def validate(self, command_parts):
        if any(cmd not in self.allowed_commands for cmd in command_parts):
            raise ValueError('Invalid command')

app = FastAPI()
command_validator = CommandValidator(['ping'])
def ping(host: str):
    # Ensure the host parameter is sanitized or validated
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    command_parts = ['ping', host]
    command_validator.validate(command_parts)
    subprocess.run(shlex.split(' '.join(command_parts)), check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)