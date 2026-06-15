from fastapi import FastAPI
import subprocess
import shlex
class HostInputValidator:
    def __init__(self, allowed_hosts):
        self.allowed_hosts = allowed_hosts

    def validate(self, host):
        return host in self.allowed_hosts

app = FastAPI()
allowed_hosts_validator = HostInputValidator(allowed_hosts=['example.com', 'localhost'])

@app.get('/ping')
def ping(host: str):
    if not allowed_hosts_validator.validate(host):
        return {'status': 'error', 'message': 'Host is not allowed'}
    try:
        result = subprocess.run(shlex.split(f'ping {host}'), capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}