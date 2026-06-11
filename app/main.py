from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate host to prevent arbitrary command execution
    if not is_valid_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        result = subprocess.run(shlex.split(f'ping {host}'), check=True, text=True, capture_output=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

def is_valid_host(host: str) -> bool:
    # Implement host validation logic here
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts