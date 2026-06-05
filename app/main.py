from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    # Add logic to validate the host input here
    return True if 'allowed_hosts' in host else False

@app.get('/ping')
def ping(host: str):
    if is_valid_host(host):
        subprocess.call(['ping', host])
        return {'status': 'completed'}
    else:
        return {'error': 'Invalid host'}, 400