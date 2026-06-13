from fastapi import FastAPI
import subprocess
import re
class Sanitizer:
    @staticmethod
def sanitize_input(host: str) -> bool:
        allowed_hosts = ['example.com', '127.0.0.1']
        return bool(re.match(r'^[a-zA-Z0-9.-]+$', host)) and host in allowed_hosts

app = FastAPI()

def ping(host: str):
    if not Sanitizer.sanitize_input(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, shell=False)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}