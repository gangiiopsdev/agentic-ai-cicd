from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def escape_host(host):
    return quote(host)

def validate_host(host):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-')
    if not all(c in allowed_chars for c in host) or '-' not in host:
        raise ValueError('Invalid host format')

@app.get('/ping')
def ping(host: str):
    try:
        validate_host(host)
        output = subprocess.check_output(['ping', escape_host(host)], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}