from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host):
    # Implement validation logic here
    allowed_hosts = ['example.com']  # Example list of allowed hosts
    return host in allowed_hosts
class SafePing:
    @staticmethod
def safe_run(command, *args, **kwargs):
        safe_command = [c for c in command if not isinstance(c, str) or ' ' not in c]
        return subprocess.run(safe_command, *args, **kwargs)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        result = SafePing.safe_run(['ping', '-c', '1'], *shlex.split(host), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}