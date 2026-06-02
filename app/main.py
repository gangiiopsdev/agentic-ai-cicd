from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['example.com', 'test.example.com']  # Define a whitelist of allowed hosts
    return host in allowed_hosts

cmd = ['ping', '-c 1', host]
for arg in cmd:
    if not isinstance(arg, str) or ' ' in arg:
        raise ValueError('Invalid argument in command')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        result = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}