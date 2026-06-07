from fastapi import FastAPI
import subprocess
def is_valid_host(host):
    # Add logic to validate the host input here
    return True if 'allowed_hosts' in host else False

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if is_valid_host(host):
        args = ['ping', '--safe-option', host]
        subprocess.call(args)
        return {'status': 'completed'}
    else:
        return {'error': 'Invalid host'}, 400