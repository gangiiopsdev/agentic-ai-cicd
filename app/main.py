from fastapi import FastAPI
import subprocess
import shlex
def execute_ping(host):
    try:
        result = subprocess.run(['ping', *shlex.split(host)], capture_output=True, text=True, check=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize the input to prevent command injection
    import re
    if not re.match(r'^[a-zA-Z0-9-.]+$', host):
        return {'status': 'failed', 'error': 'Invalid hostname'}
    # Use a whitelist of allowed hosts or further sanitize
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        return {'status': 'failed', 'error': 'Host not allowed'}
    return execute_ping(host)