from fastapi import FastAPI
import subprocess

def ping(host: str):
    # Sanitize input before using it in the subprocess call
    if not host.strip():
        return {'status': 'failed', 'error': 'Invalid host provided'}
    sanitized_host = subprocess.call(['ping', '-c', '1', host], capture_output=True, text=True)
    if sanitized_host.returncode == 0:
        return {'status': 'completed', 'output': result.stdout}
    else:
        return {'status': 'failed', 'error': result.stderr}