from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Validate input to prevent command injection
    if not host.isalpha() or len(host) > 64:
        raise ValueError('Invalid host name')
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}