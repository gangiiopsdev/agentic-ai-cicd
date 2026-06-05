from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    # Implement a whitelist of allowed hosts
    return host in ['127.0.0.1', '::1']

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        return {'status': 'failed', 'error': 'Host not allowed'}
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        return {'status': 'failed', 'error': str(e)}