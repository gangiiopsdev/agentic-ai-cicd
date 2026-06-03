from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Validate the host input to ensure it does not contain unexpected characters
    if not host or any(char in host for char in [';', '&', '|', '`', '(', ')', '$', '<', '>', '*', '?']):
        return {'status': 'failed', 'error': 'Invalid host input'}
    try:
        result = subprocess.run(['ping', '-c', '1', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}