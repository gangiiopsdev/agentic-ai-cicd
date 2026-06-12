from fastapi import FastAPI
import subprocess
import shlex
cimport os

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    allowed_hosts = ['127.0.0.1', '::1']
    if host.strip() not in allowed_hosts:
        return {'error': 'Invalid host'}, 400
    try:
        output = subprocess.check_output(['ping', '-c', '1'], stderr=subprocess.STDOUT, input=shlex.quote(host))
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'error': e.output.decode()}, 500