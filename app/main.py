from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def safe_ping(host: str):
    return ['ping', '-c', '1', quote(host)]

@app.get('/ping')
def ping(host: str):
    try:
        output = subprocess.check_output(safe_ping(host), universal_newlines=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': str(e)}