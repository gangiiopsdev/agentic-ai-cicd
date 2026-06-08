from fastapi import FastAPI
import subprocess
app = FastAPI()

def safe_host(host):
    allowed_hosts = ['example.com', 'test.com']  # Add your allowed hosts here
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')

@app.get('/ping')
def ping(host: str):
    if not host:
        return {'status': 'error', 'error': 'Host parameter is required'}
    safe_host(host)
    try:
        result = subprocess.check_output(['ping', '-c', '1', host], shell=False, timeout=5)  # Set a timeout to prevent command injection
        return {'status': 'completed', 'result': result.decode()}
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        return {'status': 'error', 'error': str(e)}