from fastapi import FastAPI
import subprocess
import shlex

class PingCommand:
    def __init__(self, host: str):
        self.host = host
        self.args = ['ping', self.host]

@app.get('/ping')
def ping(host: str):
    if not host.isalnum() or len(host) > 50:
        return {'status': 'invalid input'}, 400

    ping_command = PingCommand(host)
    subprocess.call(shlex.split(' '.join(ping_command.args)))
    return {'status': 'completed'}