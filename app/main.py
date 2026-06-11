from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate the input to prevent command injection
    if not host.isalnum():
        raise ValueError('Invalid host name')
    safe_host = subprocess.quote(host)
    result = subprocess.run(['ping', '-c', '1', safe_host], capture_output=True, text=True)
    return {'status': 'completed', 'stdout': result.stdout}