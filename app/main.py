from fastapi import FastAPI
import subprocess
import re

class SafePing:
    def __init__(self, allowed_hosts=None):
        self.allowed_hosts = allowed_hosts or []

    def validate_host(self, host: str) -> bool:
        # Validate host using regular expressions for example
        pattern = re.compile(r'^[a-zA-Z0-9.-]+$')
        return bool(pattern.match(host)) and host in self.allowed_hosts

    def run_ping(self, host: str):
        if not self.validate_host(host):
            raise ValueError('Invalid or unallowed host')
        args = ['ping', host]
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout

app = FastAPI()
safe_ping_instance = SafePing(allowed_hosts=['example.com'])

@app.get('/ping')
def ping(host: str):
    try:
        output = safe_ping_instance.run_ping(host)
        return {'status': 'completed', 'output': output}
    except ValueError as e:
        return {'status': 'error', 'message': str(e)}