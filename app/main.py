from fastapi import FastAPI
import subprocess
def ping(host: str):
    try:
        # Use subprocess.run instead of subprocess.call and avoid using shell=True
        result = subprocess.run(['ping', host], check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}