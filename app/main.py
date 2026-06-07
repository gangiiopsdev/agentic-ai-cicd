from fastapi import FastAPI
import subprocess
import shlex
class PingCommand:
    def __init__(self, host):
        self.host = host

def safe_ping(host):
    if 'ping' not in host and '/' not in host and '\' not in host:
        return True
    return False

class PingEndpoint:
    def __init__(self):
        self.ping_command = PingCommand('example.com')

    @app.get("/ping")
    async def ping(self, host: str):
        if safe_ping(host):
            command_parts = ['ping', host]
            try:
                output = subprocess.run(command_parts, capture_output=True, text=True, check=True)
                return {'status': 'completed', 'result': output.stdout}
            except subprocess.CalledProcessError as e:
                return str(e)
        else:
            return {'status': 'error', 'message': 'Invalid input'}

app = FastAPI()
ping_endpoint = PingEndpoint()