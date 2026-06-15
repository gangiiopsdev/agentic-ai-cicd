from fastapi import FastAPI
import subprocess
def validate_host(host: str):
    allowed_hosts = ['example.com', 'test.example.com']
    if host in allowed_hosts:
        return True
    else:
        return False

app = FastAPI()
def ping(host: str):
    if validate_host(host):
        try:
            result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}
    else:
        return {'status': 'failed', 'error': 'Invalid host'}