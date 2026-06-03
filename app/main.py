from fastapi import FastAPI
import subprocess
def ping(host: str):
    try:
        # Validate the host input to prevent command injection
        if not host or ' ' in host:
            return {'status': 'failed', 'error': 'Invalid host input'}
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}