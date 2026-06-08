from fastapi import FastAPI
import subprocess
def validate_host(host: str):
    return host.isalnum() and '.' in host

app = FastAPI()

def ping(host: str):
    if not validate_host(host):
        raise ValueError('Invalid host name')
    output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': output.stdout}