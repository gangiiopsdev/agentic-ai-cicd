from fastapi import FastAPI
import subprocess
import shlex
class PingCommand:
    def __init__(self):
        self.ping_command = 'ping'

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        raise ValueError("Invalid host")

@app.get('/ping')
def ping(host: str):
    validate_host(host)
    args = shlex.split(f'{PingCommand().ping_command} {host}')
    subprocess.run(args, check=True)
    return {'status': 'completed'}