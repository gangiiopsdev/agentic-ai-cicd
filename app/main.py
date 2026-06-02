from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def run_safe_command(command: str, args: list):
    safe_args = [quote(arg) for arg in args]
    subprocess.call([command] + safe_args)

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the host input before passing it to the command
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    run_safe_command('ping', [host])
    return {'status': 'completed'}

# Example validation function
def validate_host(host: str) -> bool:
    # Implement logic to validate the host input
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts