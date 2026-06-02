from fastapi import FastAPI
import subprocess
import shlex

def validate_host(host: str) -> bool:
    return '.' in host or '@' in host

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        result = subprocess.run(['ping'] + shlex.split(shlex.quote(host)), check=True, stdout=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

# Additional preventive controls to further harden the application:
# 1. Use a whitelist of allowed hosts.
# 2. Implement rate limiting on /ping endpoint.