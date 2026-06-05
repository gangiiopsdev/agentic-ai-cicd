from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_safe_host(host):
    # Define a list of allowed hosts or patterns
    safe_hosts = ['example.com', '*.example.com']
    for pattern in safe_hosts:
        if fnmatch.fnmatch(host, pattern):
            return True
    raise ValueError('Host not allowed')

@app.get('/ping')
def ping(host: str):
    if not is_safe_host(host):
        return {'status': 'failed', 'error': 'Unauthorized host'}
    try:
        result = subprocess.run(['ping'] + shlex.split(host), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}