from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        try:
            output = subprocess.check_output(['ping', self.host], stderr=subprocess.STDOUT, shell=False)
            return output.decode('utf-8')
        except subprocess.CalledProcessError as e:
            return str(e.output.decode('utf-8'))

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not PingCommand.is_valid_host(host):
        return {'status': 'error', 'result': 'Invalid host'}
    ping_command = PingCommand(host)
    result = ping_command.execute()
    return {'status': 'completed', 'result': result}

@staticmethod
def is_valid_host(host: str) -> bool:
    # Add logic to validate the host input
    import re
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None