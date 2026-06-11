from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['localhost', '127.0.0.1']
    if host not in allowed_hosts:
        raise ValueError('Unauthorized host')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    validate_host(host)
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], shell=False, universal_newlines=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}