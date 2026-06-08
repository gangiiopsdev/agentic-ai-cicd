from fastapi import FastAPI
import subprocess
import re

def ping(host: str):
    if not host or ' ' in host or ';' in host or not re.match(r'^[a-zA-Z0-9.-]+$', host):  # Validate host format
        raise ValueError('Invalid host name')
    safe_host = subprocess.shlex_quote(host)
    try:
        result = subprocess.run(['ping', '-c', '1', safe_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}