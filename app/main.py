from fastapi import FastAPI
import subprocess
import shlex
class PingCommand:
    def __init__(self, host):
        self.host = host

    def sanitize_input(self):
        return ''.join(e for e in self.host if e.isalnum())

    def execute_command(self):
        sanitized_host = self.sanitize_input()
        if not sanitized_host:
            raise ValueError('Invalid input for host')
        subprocess.call(['ping', shlex.quote(sanitized_host)])

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    return PingCommand(host).execute_command()