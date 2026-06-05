from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.safe_commands = {'ping'}

    def validate_command(self, command):
        if command not in self.safe_commands:
            raise ValueError('Invalid command')

    def execute(self, command, host):
        self.validate_command(command)
        subprocess.call([command, host])

app = FastAPI()
safe_ping = SafePing()
def validate_host(host):
    if not host.isalnum() or '.' in host:
        raise ValueError('Invalid host name')
@app.get('/ping')
def ping(host: str):
    validate_host(host)
    safe_ping.execute('ping', host)
    return {'status': 'completed'}