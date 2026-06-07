from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host):
    return host in ['example.com', 'test.example.com']  # Define a whitelist of allowed hosts
def escape_host(host):
    return ''.join(c if c.isalnum() or c in ('.', '-', '_') else '_' for c in host)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    escaped_host = escape_host(host)
    try:
        args = shlex.split('ping -c 1 ' + escaped_host)
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}