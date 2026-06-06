from fastapi import FastAPI
import subprocess
import shlex
class InputValidator:
    def __init__(self):
        self.allowed_hosts = ['127.0.0.1', '::1']

    def validate(self, host):
        if host not in self.allowed_hosts:
            raise ValueError('Invalid host')

app = FastAPI()
validator = InputValidator()

@app.get('/ping')
def ping(host: str):
    validator.validate(host)
    command = ['ping', shlex.quote(host)]
    subprocess.run(command, check=True)
    return {'status': 'completed'}