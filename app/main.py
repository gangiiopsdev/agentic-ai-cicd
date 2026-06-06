from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def ping(host: str):
    # Improved regex to validate hostname more strictly
    if not re.match(r'^[a-zA-Z0-9.-]{1,255}$', host):
        return {'status': 'failed', 'error': 'Invalid hostname'}
    try:
        result = subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}