from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def safe_ping(host):
    allowed_hosts = ['127.0.0.1', '::1']
    if host in allowed_hosts:
        args = ["ping", host]
        result = subprocess.run(args, capture_output=True, text=True, timeout=5)
        return result.stdout
    else:
        return None

@app.get('/ping')
def ping(host: str):
    try:
        output = safe_ping(host)
        if output is not None:
            return {'status': 'completed', 'output': output}
        else:
            return {'status': 'failed', 'error': 'Invalid host'}
    except subprocess.TimeoutExpired as e:
        return {'status': 'failed', 'error': 'Command timed out'}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}