from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Validate the host input to ensure it is safe
    allowed_hosts = ['example.com', '127.0.0.1']
    if host not in allowed_hosts:
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}