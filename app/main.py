from fastapi import FastAPI
import subprocess
import re

def ping(host: str):
    # Secure implementation
    if host.strip() and re.match(r'^[a-zA-Z0-9.-]+$', host):
        try:
            result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
            return {'result': 'Ping successful for ' + host}
        except subprocess.CalledProcessError as e:
            return {'error': str(e)}
    else:
        raise ValueError('Invalid host parameter')

app = FastAPI()
@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)