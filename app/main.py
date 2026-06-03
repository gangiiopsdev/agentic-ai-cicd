from fastapi import FastAPI
import subprocess
def ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid host name')
    cimport = ['ping', host]
    try:
        result = subprocess.run(cimport, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}