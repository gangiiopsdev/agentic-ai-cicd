from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def ping(host: str):
    try:
        # Sanitize the host input to prevent command injection
        if not host.isalnum() or len(host) > 255:
            raise ValueError("Invalid hostname")
        result = subprocess.run(['ping', quote(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}