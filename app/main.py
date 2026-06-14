from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def sanitize_host(host: str) -> str:
    allowed_chars = r'[a-zA-Z0-9_.-]+'
    if not re.match(allowed_chars, host):
        raise ValueError('Invalid input')

@app.get('/ping')
def ping(host: str):
    try:
        sanitized_host = sanitize_host(host)
        result = subprocess.run(['ping', '-c', '1'] + shlex.split(f'/bin/ping {sanitized_host}'), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except ValueError as e:
        return {'status': 'failed', 'error': str(e)}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}