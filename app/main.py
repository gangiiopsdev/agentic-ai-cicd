from fastapi import FastAPI
import subprocess
from shlex import quote
def safe_ping(host):
    allowed_hosts = ['example.com', 'another-example.com']
    if host in allowed_hosts:
        return True
    else:
        raise ValueError('Unauthorized host')

app = FastAPI()

@app.get("/ping")
def ping(host: str):\n    try:\n        if safe_ping(host):\n            output = subprocess.check_output(['ping', quote(host)], stderr=subprocess.STDOUT, timeout=5)\n            return {'status': 'completed', 'output': output.decode()}\n        else:\n            return {'status': 'failed', 'error': 'Unauthorized host'}\n    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:\n        return {'status': 'failed', 'error': str(e)}