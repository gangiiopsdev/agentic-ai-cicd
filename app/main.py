from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

# Define a regex pattern to allow only alphanumeric characters, dots, and hyphens
hostname_pattern = r'^[a-zA-Z0-9.-]+$'

def ping(host: str):
    if not re.match(hostname_pattern, host):
        return {'status': 'failed', 'output': 'Invalid hostname'}
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'output': str(e)}
    return {'status': 'completed', 'output': result.stdout}