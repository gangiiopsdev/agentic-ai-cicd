from fastapi import FastAPI
import shlex
import re
import subprocess
class SafePing:
    def __init__(self):
        self.allowed_chars = r'^[a-zA-Z0-9.-]+$'

    def validate_host(self, host: str):
        if not re.match(self.allowed_chars, host):
            raise ValueError('Invalid hostname')

    def run_command(self, args: list):
        try:
            result = subprocess.run(args, check=True, capture_output=True, text=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return str(e)

app = FastAPI()
safe_ping_instance = SafePing()

def safe_ping(host: str):
    safe_ping_instance.validate_host(host)
    args = shlex.split(f'ping {host}')
    return safe_ping_instance.run_command(args)

@app.get('/ping')
def ping(host: str):
    output = safe_ping(host)
    return {'status': 'completed', 'output': output}