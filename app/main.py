from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['8.8.8.8', '127.0.0.1']  # Example allowed hosts
    ip_pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'
    if re.match(ip_pattern, host) and host in allowed_hosts:
        return True
    return False

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        args = shlex.split(f'ping {host}')
        try:
            result = subprocess.run(args, check=True, capture_output=True, text=True)
            return {'status': 'completed', 'output': result.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}
    else:
        return {'status': 'failed', 'error': 'Invalid host'}