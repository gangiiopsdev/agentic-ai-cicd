from fastapi import FastAPI
import subprocess
from shlex import quote as cmd_quote
class PingCommand:
    def __init__(self, host):
        self.host = host

    def ping(self):
        try:
            output = subprocess.check_output([cmd_quote('ping'), '-c 1', cmd_quote(self.host)], stderr=subprocess.STDOUT, text=True)
            return {'status': 'completed', 'output': output}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.output}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    ping_command = PingCommand(host)
    try:
        output = subprocess.check_output([cmd_quote('ping'), '-c 1', cmd_quote(host)], stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output}