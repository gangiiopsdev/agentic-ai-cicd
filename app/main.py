from fastapi import FastAPI
import subprocess
import shlex
def is_valid_host(host):
    # Simple regex to validate host
    import re
    return bool(re.match(r'^[a-zA-Z0-9.-]+$', host))

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not is_valid_host(host):
        return {'error': 'Invalid host'}, 400
    args = ['ping'] + shlex.split(host)
    result = subprocess.run(args, capture_output=True, text=True, check=False, shell=False)
    return {'status': 'completed', 'output': result.stdout}