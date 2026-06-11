from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['8.8.8.8', '127.0.0.1']
    return host in allowed_hosts

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, universal_newlines=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output}