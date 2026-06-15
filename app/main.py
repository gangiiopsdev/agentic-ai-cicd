from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Sanitize input
    if not host.strip().replace('.', '').isdigit():
        return {'status': 'failed', 'error': 'Invalid hostname'}
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=10)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}