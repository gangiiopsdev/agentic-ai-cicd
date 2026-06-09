from fastapi import FastAPI
import subprocess
import shlex

def ping(host: str):
    # Ensure host input is sanitized to prevent injection attacks
    allowed_hosts = ['127.0.0.1', 'localhost']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    cmd = ['ping', shlex.quote(host)]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed'}