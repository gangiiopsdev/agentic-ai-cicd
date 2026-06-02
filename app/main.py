from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_safe_host(host):
    safe_hosts = ['127.0.0.1', '::1']  # Define a list of safe hosts
    return host in safe_hosts

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        command = ['ping', host]
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}