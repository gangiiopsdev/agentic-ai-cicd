from fastapi import FastAPI
import subprocess
from urllib.parse import urlparse
class SafeSubprocess:
    @staticmethod
def run(command: str, *args, **kwargs):
        full_command = [command] + list(args)
        return subprocess.run(full_command, shell=False, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

app = FastAPI()

async def safe_ping(host: str):
    if not is_valid_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    try:
        result = SafeSubprocess.run('ping', '-c', '1', shlex.quote(host))  # Added shlex.quote here
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)
def is_valid_host(host: str) -> bool:
    # Use regex to validate the host format (e.g., domain or IP address)
    pattern = re.compile(r'^[a-zA-Z0-9.-]+$')
    if not pattern.match(host):
        return False
    # Optionally, add additional validation logic here
    allowed_hosts = ['example.com', '127.0.0.1']
    return host in allowed_hosts