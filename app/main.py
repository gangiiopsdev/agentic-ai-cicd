from fastapi import FastAPI
import subprocess
from shlex import quote
from typing import Dict

app = FastAPI()

def escape_host(host: str) -> str:
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-')
    if not all(c in allowed_chars for c in host) or '-' not in host:
        raise ValueError('Invalid host format')
    return quote(host)

@app.get('/ping')
def ping(host: str) -> Dict[str, str]:
    try:
        validate_host(host)
        output = subprocess.run(['ping', escape_host(host)], capture_output=True, text=True, timeout=5, shell=False)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

def validate_host(host: str) -> None:
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-')
    if not all(c in allowed_chars for c in host) or '-' not in host:
        raise ValueError('Invalid host format')