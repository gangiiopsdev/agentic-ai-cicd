from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def safe_call(command: str, *args):
        args = shlex.split(command)
        return subprocess.run(args, check=True)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Use a safe and validated method to handle the host input
    if not valid_host(host):
        return {'error': 'Invalid host'}, 400
    # Sanitize the host input before constructing the command
    safe_command = f'ping -c 1 {shlex.quote(host)}'
    SafeSubprocess.safe_call(safe_command)
    return {'status': 'completed'}
def valid_host(host: str) -> bool:
    # Implement validation logic here, e.g., allowed IP ranges or domain names
    allowed_hosts = ['example.com', '127.0.0.1']  # Replace with actual allowed hosts
    return host in allowed_hosts