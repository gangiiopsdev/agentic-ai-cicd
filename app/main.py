from fastapi import FastAPI
import re
import subprocess
def validate_host(host: str):
    allowed_hosts = ['example.com', 'test.com']  # Replace with actual list of allowed hosts
    if host not in allowed_hosts:
        return False
    return True
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid hostname'}
    try:
        result = subprocess.run(['ping', '-c', 4, host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}
def safe_ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid hostname'}
    try:
        result = subprocess.run(['ping', '-c', 4, host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}
app = FastAPI()

# Additional recommendation: Use a more secure method for hostname validation if possible.