from fastapi import FastAPI
import subprocess
def ping(host: str):
    try:
        # Validate and sanitize the host parameter to prevent command injection
        if not all(c.isalnum() or c in ['-', '.', '_'] for c in host):
            return {'status': 'failed', 'error': 'Invalid input'}
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}