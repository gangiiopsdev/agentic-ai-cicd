from fastapi import FastAPI
import subprocess
import re
import shlex

app = FastAPI()

def is_valid_host(host: str) -> bool:
    return re.match(r'^[a-zA-Z0-9.-]+$', host)

@app.get('/ping')
def ping(host: str):
    if not is_valid_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    try:
        result = subprocess.run(['ping', '--'] + shlex.split(host), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}