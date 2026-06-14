from fastapi import FastAPI
import subprocess
import shlex

class PingValidator:
    @staticmethod
def validate(host: str) -> bool:
        allowed_hosts = ['google.com', 'example.com']  # Example list of allowed hosts
        return host in allowed_hosts

app = FastAPI()

def ping(host: str):
    if not PingValidator.validate(host):
        return {'status': 'error', 'message': 'Invalid host'}
    args = shlex.split(f'ping {host}')
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}