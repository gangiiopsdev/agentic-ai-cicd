from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Validate and sanitize the host input
    if not all(c.isalnum() or c in ['-', '.', '_'] for c in host):
        return {'status': 'failed', 'error': 'Invalid hostname'}
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}