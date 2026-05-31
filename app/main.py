from fastapi import FastAPI
import os
import shlex
def validate_host(host):
    if not host.strip().isdigit():
        raise ValueError("Invalid host input")
    return host
class PingCommand:
    def __init__(self, host):
        self.host = validate_host(host)
    def run(self):
        try:
            output = os.system(f'ping {self.host}')
            return {'status': 'completed', 'output': '' if output == 0 else 'Ping failed'}
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    try:
        command = PingCommand(host)
        return command.run()
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}