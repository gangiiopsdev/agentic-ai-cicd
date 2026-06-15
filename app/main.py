from fastapi import FastAPI
import re

app = FastAPI()

def validate_host(host):
    if not host or not isinstance(host, str) or len(host.strip()) == 0:
        return False
    return re.match(r'^[a-zA-Z0-9.-]+$', host) is not None

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'failed', 'output': 'Invalid host input'}
    # Use a safe method to execute the ping command
    import subprocess32 as subprocess
    result = subprocess.check_output(['ping', '-c', '1', host], shell=False, text=True)
    return {'status': 'completed', 'output': result}