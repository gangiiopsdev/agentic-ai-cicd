from fastapi import FastAPI
import subprocess
import shlex
import re
def sanitize_input(input_str):
    return ''.join(e for e in input_str if e.isalnum() or e in ('-', '.'))
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    # Validate and sanitize input to prevent command injection
    sanitized_host = sanitize_input(host)
    if not re.match(r'^[a-zA-Z0-9.-]+$', sanitized_host):
        raise ValueError('Invalid hostname')
    try:
        result = subprocess.run(shlex.split(f'ping {sanitized_host}'), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return {'status': 'completed', 'stdout': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'stderr': e.stderr}