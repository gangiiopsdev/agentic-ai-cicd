from fastapi import FastAPI
import subprocess
def ping_host(host):
    if isinstance(host, str) and any(char in host for char in ['&&', ';', '|', '`']):
        raise ValueError('Invalid characters in host name')
    cmd = ['ping', host]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}