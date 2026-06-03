from fastapi import FastAPI
import subprocess
import shlex
import re

class PingCommand:
    def __init__(self):
        self.args = ['ping']

    def add_host(self, host: str):
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            raise ValueError(f'Invalid host name: {host}')
        try:
            self.args += shlex.split(host)
        except Exception as e:
            raise ValueError(f'Invalid host name: {host}')

    def execute(self):
        result = subprocess.run(self.args, capture_output=True, text=True, check=False)
        return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    ping_command = PingCommand()
    try:
        ping_command.add_host(host)
        return ping_command.execute()
    except ValueError as e:
        return {'error': str(e), 'status': 'failed'}