from fastapi import FastAPI, HTTPException
import subprocess
def is_valid_host(host):
    allowed_hosts = ['127.0.0.1', '::1']  # Add more hosts as needed
    return host in allowed_hosts

global_allowed_hosts = set(['127.0.0.1', '::1'])

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not is_valid_host(host):
        raise HTTPException(status_code=422, detail='Invalid host')
    try:
        output = subprocess.check_output(['ping', '-c 1', host], stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e.output)}