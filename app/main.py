from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_valid_host(host):
    allowed_hosts = ['127.0.0.1', '::1']  # Add valid hosts here
    return host in allowed_hosts

@app.get('/ping')
def ping(host: str):
    if not is_valid_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    result = subprocess.run(['ping', *shlex.split(shlex.quote(host))], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}