from fastapi import FastAPI
import re
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Validate the host input to ensure it is a valid hostname or IP address
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'failed', 'error': 'Invalid host input'}
    # Use parameterized commands instead of directly passing arguments to avoid command injection
    try:
        result = subprocess.run(['ping', '-c', '1', f'"{host}"'], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}