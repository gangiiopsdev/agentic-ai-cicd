from fastapi import FastAPI
import subprocess
import shlex
globally_whitelisted_hosts = ['host1', 'host2']

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if host in globally_whitelisted_hosts:
        subprocess.run(['ping', '-c 1', host], check=True, capture_output=True)  # Use subprocess.run for safer execution
    else:
        raise ValueError('Host not allowed')
    return {'status': 'completed'}