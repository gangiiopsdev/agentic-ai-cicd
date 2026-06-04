from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

# Regex pattern to validate IP address
IP_PATTERN = r'^\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b$'

def ping(host: str):
    if not re.match(IP_PATTERN, host):
        raise ValueError('Invalid host address')
    # Secure implementation using subprocess.run with shell=False
    result = subprocess.run(['ping', '-c', '4', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}