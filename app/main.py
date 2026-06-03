from fastapi import FastAPI
import subprocess
from subprocess import Popen, PIPE, DEVNULL

app = FastAPI()

def ping(host: str):
    try:
        if not is_valid_host(host):
            return {'error': 'Invalid host'}
        process = Popen(['ping', host], shell=False, stdout=DEVNULL, stderr=PIPE)
        output, error = process.communicate()
        if process.returncode == 0:
            return {'status': 'completed'}
        else:
            return {'error': str(error.decode('utf-8'))}
    except Exception as e:
        return {'error': str(e)}
def is_valid_host(host: str) -> bool:
    return host.replace('.', '').isalnum() and len(host.split('.')) == 4