from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def is_valid_host(host):
    return re.match(r'^[a-zA-Z0-9.-]+$', host) and not re.match(r'^\d+\.\d+\.\d+\.\d+$', host)

def ping(host: str):
    if not is_valid_host(host):
        raise ValueError('Invalid hostname or IP address')

    # Use subprocess.Popen for better control over the process
    try:
        result = subprocess.Popen(['ping', '-c', '1', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = result.communicate()
        if result.returncode != 0:
            raise Exception(error.decode())
        return {'status': 'completed'}
    except Exception as e:
        raise ValueError(f'Error pinging {host}: {str(e)}')