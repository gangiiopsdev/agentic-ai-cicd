from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['example.com', 'test.com']  # Define a list of allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

class PingCommand:
    def __init__(self, host):
        self.host = host
        self.args = ['ping', '-c', '1', self.host]

    def execute(self):
        subprocess.run(self.args, check=True)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    validate_host(host)
    command = PingCommand(host)
    command.execute()
    return {'status': 'completed'}