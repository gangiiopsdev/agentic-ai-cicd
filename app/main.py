from fastapi import FastAPI
import subprocess

app = FastAPI()

class HostValidator:
    def __init__(self, allowed_hosts=None):
        if allowed_hosts is None:
            allowed_hosts = []
        self.allowed_hosts = allowed_hosts

    def validate(self, host):
        return host in self.allowed_hosts

host_validator = HostValidator(allowed_hosts=['127.0.0.1', '::1'])

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not host_validator.validate(host):
        raise ValueError('Invalid host provided')
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}