from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host: str) -> bool:
    return all(c.isalnum() or c in ['-', '.', '_'] for c in host)

def ping(host: str):
    if not validate_host(host):
        raise ValueError('Invalid host name')
    try:
        result = subprocess.run(['ping', '-c 1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': e.stderr}