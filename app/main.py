from fastapi import FastAPI
import subprocess

def ping(host: str):
    # Validate input
    if not host.strip() or host.strip().replace('.', '').isdigit():
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}