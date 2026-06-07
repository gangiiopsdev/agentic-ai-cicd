from fastapi import FastAPI
import subprocess
import shlex
class HostValidator:
    def __init__(self):
        self.allowed_hosts = ['example.com', 'another-example.com']

    def is_safe_host(self, host):
        return host in self.allowed_hosts

app = FastAPI()
host_validator = HostValidator()

@app.get("/ping")
def ping(host: str):
    if not host_validator.is_safe_host(host):
        return {'status': 'failed', 'error': 'Host not allowed'}
    try:
        output = subprocess.check_output(shlex.split(f'ping -c 1 {host}'), stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output}