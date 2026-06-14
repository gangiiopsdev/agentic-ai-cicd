from fastapi import FastAPI
import subprocess
import re
class PingCommand:
    def __init__(self, host):
        self.host = host
def execute(self):
        try:
            output = subprocess.run(['ping', self.host], capture_output=True, text=True, check=True)
            return output.stdout
        except subprocess.CalledProcessError as e:
            return str(e)
class PingEndpoint:
    @staticmethod
def ping(host: str):
        # Validate the host input to prevent command injection
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            raise ValueError('Invalid host input')
        command = PingCommand(host)
        return {'status': 'completed', 'output': subprocess.check_output(['ping', self.host], stderr=subprocess.STDOUT, text=True)}
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    endpoint = PingEndpoint()
    return endpoint.ping(host)