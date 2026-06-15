from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def is_valid_host(host):
    return re.match(r'^[a-zA-Z0-9.-]+$', host) and not re.match(r'^\d+\.\d+\.\d+\.\d+$', host)

@app.get('/ping')
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError('Invalid hostname or IP address')
    subprocess.run(['ping', '-c', '1', f'{host}'], check=True, shell=False)
    return {'status': 'completed'}