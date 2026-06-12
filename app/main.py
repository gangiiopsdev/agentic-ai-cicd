from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Validate and sanitize host input
    if not host.strip() or ' ' in host:
        return {'status': 'failed', 'error': 'Invalid host name'}
    try:
        result = subprocess.run(['ping', '--', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}