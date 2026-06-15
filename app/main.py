from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    valid_hosts = ['192.168.', '10.0.']
    for valid_host in valid_hosts:
        if host.startswith(valid_host):
            return True
    return False

@app.get('/ping')
def ping(host: str):
    if is_valid_host(host):
        command = ['ping', host]
        subprocess.run(command, check=True)
        return {'status': 'completed'}
    else:
        return {'error': 'Invalid host'}