from fastapi import FastAPI
import subprocess
import shlex

class HostValidator:
    def __init__(self, allowed_hosts=None):
        self.allowed_hosts = allowed_hosts or []

    def validate(self, host):
        if not any(host.startswith(allowed_host) for allowed_host in self.allowed_hosts):
            raise ValueError(f'Host {host} is not allowed')

app = FastAPI()
validator = HostValidator(allowed_hosts=['192.168.1.', 'localhost'])

@app.get('/ping')
def ping(host: str):
    validator.validate(host)
    try:
        output = subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}