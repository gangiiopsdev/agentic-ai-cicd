from fastapi import FastAPI
import subprocess
def ping(host: str):
    if not host.isalnum():
        return {'status': 'error', 'error': 'Invalid host'}
    try:
        subprocess.run(['ping', host], check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': str(e)}