from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def ping(host: str):
    try:
        # Validate the host input to ensure it does not contain malicious content
        if not is_valid_host(host):
            raise ValueError('Invalid host')
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}
def is_valid_host(host: str) -> bool:
    # Implement validation logic here
    return host.isalnum() and '.' in host