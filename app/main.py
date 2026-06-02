from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    def __init__(self):
        self.command = 'ping'

    def run(self, host: str):
        if not self.is_safe_host(host):
            raise ValueError('Invalid host')
        cmd = [self.command, host]
        subprocess.run(cmd, check=True)

app = FastAPI()
pinger = SafePing()

@app.get('/ping')
def ping(host: str):
    try:
        pinger.run(host)
        return {'status': 'completed'}
    except ValueError as e:
        return {'error': str(e)}, 400