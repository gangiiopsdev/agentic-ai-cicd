from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    safe_hosts = ['localhost', '127.0.0.1']
    return host in safe_hosts

@app.get('/ping')
def ping(host: str):
    if not is_safe_host(host):
        return {'status': 'failed', 'error': 'Host is not allowed'}
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output}