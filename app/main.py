from fastapi import FastAPI
import subprocess
import re

def validate_host(host):
    return re.match(r'^[a-zA-Z0-9.-]+$', host)

@app.get('/ping')
def ping(host: str):    
    if not validate_host(host):
        return {'error': 'Invalid host'}, 400

    # Use a fully qualified path for the command to mitigate risks and avoid shell=True
    subprocess.run(['/usr/bin/ping', '-c', '1', host], check=True, shell=False)
    return {'status': 'completed'}