from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host):
    # Implement a simple whitelist of allowed hosts
    allowed_hosts = ['8.8.8.8', '127.0.0.1']
    return host in allowed_hosts

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        # Use shlex to safely split the command string
        args = ['ping', '-c', '1'] + shlex.split(host)
        output = subprocess.check_output(args, stderr=subprocess.STDOUT, universal_newlines=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output}