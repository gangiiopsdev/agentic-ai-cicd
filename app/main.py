from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    try:
        # Sanitize the host input to prevent command injection
        if not host.isalnum():
            raise ValueError('Invalid host name')
        result = subprocess.run(['ping', '-c 1 ' + shlex.quote(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}