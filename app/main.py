from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_valid_host(host):
    # Add logic to validate host input
    return host.strip().endswith('.com')

@app.get('/ping')
def ping(host: str):
    if not is_valid_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    args = ['ping', host]
    subprocess.call(args)
    return {'status': 'completed'}