from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Validate and sanitize the host input
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    result = subprocess.run(['ping', '-c', '4', host], capture_output=True, text=True)
    return {'status': 'completed', 'result': result.stdout}