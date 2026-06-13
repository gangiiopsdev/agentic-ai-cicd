from fastapi import FastAPI
import subprocess
import re

class PingCommand:
    def __init__(self, host):
        self.host = host

    def execute(self):
        args = ['ping', self.host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout

def validate_host(host: str) -> bool:
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None

app = FastAPI()

@app.get("/ping")
def ping(host: str = 'example.com'):  # Use a default safe value for host
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    result = PingCommand(host).execute()
    return {'status': 'completed', 'result': result}