from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    def __call__(self, *args):
        return self.run(*args)

    @staticmethod
def run(command: str, *args, **kwargs):
        args = shlex.split(command)
        if not validate_command(args):
            raise ValueError('Invalid command')
        return subprocess.run(args, check=True, **kwargs)
class SafePing:
    def __init__(self):
        self.safe_subprocess = SafeSubprocess()

    def ping(self, host: str):
        if not validate_host(host):
            return {'error': 'Invalid host'}
        command = f'ping {host}'
        result = self.safe_subprocess.run(command)
        return {'status': 'completed', 'output': result.stdout.decode('utf-8')}

app = FastAPI()
def validate_host(host):
    return 'localhost' in host or '127.0.0.1' in host
def validate_command(command):  # Simple validation, replace with more robust checks
    for arg in command:
        if not isinstance(arg, str) or '&&' in arg or ';' in arg or '|' in arg:
            return False
    return True
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
ping_instance = SafePing()

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'error': 'Invalid host'}
    command = f'ping {host}'
    result = ping_instance.safe_subprocess.run(command)
    return {'status': 'completed', 'output': result.stdout.decode('utf-8')}